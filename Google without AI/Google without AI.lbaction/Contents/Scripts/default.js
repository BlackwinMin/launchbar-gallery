//
// LaunchBar Action
//

function runWithString(argument)
{
    LaunchBar.openURL('https://www.google.com/search?q=' + encodeURIComponent(argument) + '&udm=14');
}