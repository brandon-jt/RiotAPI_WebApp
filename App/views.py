from django.shortcuts import render
import requests
import time
import mysql.connector
import configparser


def getRequest(apiurl):
    """ Handles API requests and returns the request as json. If a rate-limiting 429 status code is in the request,
        sleeps for the Retry-After and tries again"""
    getterObject = requests.get(apiurl)
    statusCode = getterObject.status_code
    if statusCode == 429:                                           # if Status Code denotes rate limited
        time.sleep(int(getterObject.headers.get('Retry-After')))    # Sleep for the 'Retry-After' amount
        getterObject = requests.get(apiurl)                         # And send the request again
    return getterObject.json()


def EnterName(request):
    """ Called after the Name is submitted on the page."""
    template_name = "App/EnterName.html"
    return render(request, template_name)


def createConnection():
    """ Creates the connection to the database using the credentials from the .ini file, returns connector """
    config = configparser.ConfigParser()    # Config parser to get the Database data and API Key from the ini file
    # config.read('/Users/brandonturner/PycharmProjects/AWSRiotAPI/App/dev.ini')
    # config.read('/PycharmProjects/AWSRiotAPI/App/dev.ini')
    config.read('C:\\Users\\brandon.turner\\PycharmProjects\\AWSRiotAPI\\App\\dev.ini')
    return mysql.connector.connect(user=config['DEFAULT'].get('user'),
                                   password=config['DEFAULT'].get('password'),
                                   host=config['DEFAULT'].get('host'),
                                   port=config['DEFAULT'].get('port'), database=config['DEFAULT'].get('database'))


def formatName(request):
    """ Capitalizes names and removes spaces to match Data Dragon naming conventions"""
    try:
        champIDbefore = request.GET.get('name')
        return champIDbefore.title().replace(" ", "")
    except KeyError:
        print("Please enter a valid champion name")


def invalidName(champs, champID):
    """ Checks to make sure the requested champion name is valid,
        returns to the landing page if invalid champion name  """
    try:
        int(champs["data"][str(champID)]["key"])           # this checks to see if the entry is actually in champs list
        return {
            'nonValidChamp': False
        }
    except KeyError:
        nonValidChampBool = {
            'nonValidChamp': True
        }
        return nonValidChampBool


def buildRenderDict(RuneNames, RuneIcons, champItemsIcons, champItemsNames):
    """ Build dictionary to pass to render for the items and runes, the dictionary will be used to feed the rune
        names, rune icons, item icons, and item names to the webpage to be rendered. """
    renderDict = {
        'rune0': RuneNames[0],
        'rune1': RuneNames[1],
        'rune2': RuneNames[2],
        'rune3': RuneNames[3],
        'rune4': RuneNames[4],
        'rune5': RuneNames[5],
        'perkPrimaryStyle': RuneNames[6],
        'perkSubStyle': RuneNames[7],
        'irune0': RuneIcons[0],
        'irune1': RuneIcons[1],
        'irune2': RuneIcons[2],
        'irune3': RuneIcons[3],
        'irune4': RuneIcons[4],
        'irune5': RuneIcons[5],
        'iperkPrimaryStyle': RuneIcons[6],
        'iperkSubStyle': RuneIcons[7]

    }
    """ Adds the item icons and the item names to the render dictionary"""

    for i in range(len(champItemsIcons)):
        champItemIconEntry = 'item' + str(i)  # renames creates item1, item2, ...
        champItemNameEntry = 'name' + str(i)  # renames itemName1, itemName2, ...
        renderDict[champItemIconEntry] = champItemsIcons[i]  # adds to renderDict
        renderDict[champItemNameEntry] = champItemsNames[i]
    return renderDict


def Begin(request):
    """ Begin is called after the Champion Name is submitted in the web app. This will create a connection
    to the database, validate and formats the champion name, then retrives the information from the database
    and passes it on to be rendered on the web page. """
    champItemsIcons = []
    champItemsNames = []
    RuneIcons = []
    RuneNames = []
    champj = requests.get("http://ddragon.leagueoflegends.com/cdn/11.16.1/data/en_US/champion.json")
    champs = champj.json()

    connection = createConnection()
    champID = formatName(request)
    nonValidChampBool = invalidName(champs, champID)
    if nonValidChampBool.get('nonValidChamp'):
        return render(request, "App/EnterName.html", nonValidChampBool)

    """ Makes an sql query to the database to fetch the items from the AWS Database """

    cursor = connection.cursor()
    cursor.execute("SELECT Item0, Item1, Item2, Item3, Item4, Item5, Item6 FROM"
                   + " ChampItems WHERE ChampName=" + "'" + champID + "'")
    queryResult = cursor.fetchall()  # Formats the rows into queryResult
    for i in range(len(queryResult[0])):
        champItemsIcons.append(queryResult[0][i])  # Adds the queried results to the list
        champItemsIcons[i] += '.png'  # append .png to the results

    uriPreHomeItem = "\\media\\item\\"  # prepend this to the x.png to get correct file path
    uriPreHomeItem += '{0}'  # needed to use .format
    champItemsIcons = [uriPreHomeItem.format(item) for item in champItemsIcons]  # becomes \\media\\item\x.png

    """ SQL query to get the rune names and images from the database """

    cursorRunes = connection.cursor()
    cursorRunes.execute("SELECT perk0, perk1, perk2, perk3, perk4, perk5,"
                        + "perkPrimaryStyle, perkSubStyle FROM ChampRunes WHERE ChampName=" + "'" + champID + "'")
    queryResultRunes = cursorRunes.fetchall()

    for i in range(len(queryResultRunes[0])):  # Iterates through query result
        val = queryResultRunes[0][i]
        updatedVal = val.title().replace(":", "").replace(" ", "")  # strips colons and spaces
        updatedVal += '.png'  # Appends required .png
        RuneIcons.append(updatedVal)
        RuneNames.append(val)

    """ SQL query to get the item names from the database """
    cursorItemNames = connection.cursor()
    cursorItemNames.execute("SELECT ItemName0, ItemName1, ItemName2, ItemName3, ItemName4, ItemName5, ItemName6 FROM"
                            + " ChampItems WHERE ChampName=" + "'" + champID + "'")
    queryResultItemNames = cursorItemNames.fetchall()       # puts the results into a list
    for i in range(len(queryResultItemNames[0])):
        champItemsNames.append(queryResultItemNames[0][i])  # adds the item names to its list from the query

    """ Prepends the directory location of the rune images to the runes in RuneIcons list """
    uriPreHomeRune = "\\media\\perk-images\\"
    uriPreHomeRune += '{0}'
    RuneIcons = [uriPreHomeRune.format(rune) for rune in RuneIcons]

    renderDict = buildRenderDict(RuneNames, RuneIcons, champItemsIcons, champItemsNames)
    connection.close()
    return render(request, 'app/Begin.html', renderDict)

