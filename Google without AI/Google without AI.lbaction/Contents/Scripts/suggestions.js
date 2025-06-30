//
// LaunchBar Action
//

function runWithString(argument)
{
    var result = HTTP.getJSON('https://suggestqueries.google.com/complete/search?client=firefox&q=' + encodeURIComponent(argument), 5);

    if (result == undefined) {
        LaunchBar.log('HTTP.getJSON() returned undefined');
        return [];
    }
    if (result.error != undefined) {
        LaunchBar.log('Error in HTTP request: ' + result.error);
        return [];
    }

    try {
        var suggestions = [];
        for (var i = 0; i < result.data[1].length; i++) {
            suggestions.push({
                'title' : JSON.stringify(result.data[1][i]).slice(1, -1),
                'icon' : 'font-awesome:fa-google'
            });
        }
        return suggestions;
    } catch (exception) {
        LaunchBar.log('Exception while parsing result: ' + exception);
        return [];
    }
}
