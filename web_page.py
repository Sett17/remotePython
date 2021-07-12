def web_page():
  html = """
<html lang="en" class="themeDark">
<head>
    <meta charset="UTF-8">
    <link rel="manifest" href="manifest.webmanifest">
    <title>Hafenstrasse Remote</title>
    <link rel="stylesheet" href="colors.css">
    <style>
        .white:after {
            background-color: floralwhite !important;
        }
        .white{
            border-color: hsl(40, 100%, 100%) !important;
            box-shadow: inset floralwhite 0 0 calc(var(--spreadWidth)/4),
             floralwhite 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .red:after {
            background-color: red;
        }
        .red{
            border-color: hsl(0, 100%, 70%) !important;
            box-shadow: inset red 0 0 calc(var(--spreadWidth)/4),
             red 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .green:after {
            background-color: green;
        }
        .green{
            border-color: hsl(120, 100%, 45%) !important;
            box-shadow: inset green 0 0 calc(var(--spreadWidth)/4),
             green 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .blue:after {
            background-color: blue;
        }
        .blue{
            border-color: hsl(240, 100%, 70%) !important;
            box-shadow: inset blue 0 0 calc(var(--spreadWidth)/4),
             blue 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .orange:after {
            background-color: orange;
        }
        .orange{
            border-color: hsl(39, 100%, 70%) !important;
            box-shadow: inset orange 0 0 calc(var(--spreadWidth)/4),
             orange 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .teal:after {
            background-color: teal;
        }
        .teal{
            border-color: hsl(180, 100%, 45%) !important;
            box-shadow: inset teal 0 0 calc(var(--spreadWidth)/4),
             teal 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .purple:after {
            background-color: purple;
        }
        .purple{
            border-color: hsl(300, 100%, 45%) !important;
            box-shadow: inset purple 0 0 calc(var(--spreadWidth)/4),
             purple 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .yellow:after {
            background-color: yellow;
        }
        .yellow{
            border-color: hsl(60, 100%, 70%) !important;
            box-shadow: inset yellow 0 0 calc(var(--spreadWidth)/4),
             yellow 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .lightblue:after {
            background-color: lightblue;
        }
        .lightblue{
            border-color: hsl(195, 53%, 95%) !important;
            box-shadow: inset lightblue 0 0 calc(var(--spreadWidth)/4),
             lightblue 0 0 calc(var(--spreadWidth)/4) !important;
        }
        .hotpink:after {
            background-color: hotpink;
        }
        .hotpink{
            border-color: hsl(330, 100%, 90%) !important;
            box-shadow: inset hotpink 0 0 calc(var(--spreadWidth)/4),
             hotpink 0 0 calc(var(--spreadWidth)/4) !important;
        }
        /*region darkcolors*/
        .themeDark {
            --backgroundColor: hsl(0, 0%, 5%);

            --neonTopColor: hsl(286, 67%, 76%);
            --neonSpreadColor: hsl(281, 75%, 38%);

            --textColor: floralwhite;

            --borderWidth: .7em;
            --spreadWidth: 3em;
        }
        /*endregion*/
        *:focus {
            outline: none;
        }

        body,
        html {
            margin: 0;
            padding: 0;
            background-color: var(--backgroundColor);
            color: var(--textColor);
            font-family: sans-serif;
        }

        #root {
            padding: 3vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-content: center;
        }

        .deviceWrapper {
            display: flex;
            background-color: var(--backgroundColor);
            min-height: 100px;
            align-self: center;
            max-width: 800px;
            width: 100%;
            margin-bottom: 3vh;
            flex-direction: column;
            align-content: center;
            justify-content: center;
            border-radius: 7vh;
            border: var(--borderWidth) var(--neonTopColor) solid;
            box-shadow: inset var(--neonSpreadColor) 0px 0px var(--spreadWidth);
            padding: 2vh;
        }

        .buttonCluster {
            display: flex;
            flex-direction: column;
            margin-top: 2vh;
            margin-bottom: 2vh;
        }

        .clusterItem {
            margin: 0;
            flex: .4;
        }

        .deviceInput.clusterItem {
            margin: 1vh;
            height: 8vh;
        }

        .deviceInput {
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            align-self: center;
            text-align: center;
            height: 12vh;
            width: 85%;
            margin-top: 2vh;
            margin-bottom: 2vh;
            background-color: var(--backgroundColor);
            border-radius: 3vh;
            font-size: 1.8vh;
            border: calc(var(--borderWidth)/3) var(--neonTopColor) solid;
            box-shadow: var(--neonSpreadColor) 0 0 calc(var(--spreadWidth)/2);
        }

        .deviceInput:hover {
            box-shadow: inset var(--neonSpreadColor) 0 0 calc(var(--spreadWidth)/3);
        }

        .deviceSwitch {
            font-size: 2.5vh;
            color: var(--textColor);
        }


        .deviceTitle {
            /*display: flex;*/
            font-size: 4vh;
            font-weight: bold;
            margin: 2vh;
            width: 100%;
            text-align: center;
        }

        .deviceInputClick {
            background-color: floralwhite;
            color: #000;
        }

        .buttonRow {
            display: flex;
            flex-direction: row;
            justify-content: space-evenly;
        }

        .colorBtn {
            width: 6.5vh;
            height: 6.5vh;
            border-radius: 100vh;
        }

        .colorBtn:after {
            content: '';
            display: block;
            width: 4vh;
            height: 4vh;
            border-radius: 100vh;
            transition: filter 50ms;
        }

        .colorBtn:hover {
            border-color: floralwhite !important;
        }

        .colorBtn:hover:after {
            filter: brightness(.7);
        }

        .ipInput {
            border-radius: 100vh;
            color: var(--textColor);
            background-color: var(--backgroundColor);
            animation: in forwards;
            border: none;
            text-align: center;
            font-size: 2.5vh;
            width: 75%;
            align-self: center;
            height: 6vh;
        }

        a {
            color: var(--textColor);
            margin-top: 2vh;
            align-self: center;
            text-decoration: underline;
        }

        a:visited {
            color: var(--textColor);
        }
    </style>
    <script>
        function send(path) {
            console.log(path)
            fetch(path)
        }
    </script>
</head>

<body style="user-select: none;" data-new-gr-c-s-check-loaded="14.1021.0" data-gr-ext-installed="">
    <div id="root">

        <div class="deviceWrapper">
            <h2 class="deviceTitle">LED's</h2>
            <div class="deviceInput deviceSwitch" onclick="send('/led/toggle/')">TOGGLE</div>
            <div class="buttonRow">
                <div class="deviceInput colorBtn red" onclick="send('/led/red')"></div>
                <div class="deviceInput colorBtn green" onclick="send('/led/green')"></div>
                <div class="deviceInput colorBtn blue" onclick="send('/led/blue')"></div>
                <div class="deviceInput colorBtn white" onclick="send('/led/white')"></div>
            </div>
            <div class="buttonRow">
                <div class="deviceInput colorBtn orange" onclick="send('/led/orange')"></div>
                <div class="deviceInput colorBtn teal" onclick="send('/led/teal')"></div>
                <div class="deviceInput colorBtn purple" onclick="send('/led/purple')"></div>
            </div>
            <div class="buttonRow">
                <div class="deviceInput colorBtn yellow" onclick="send('/led/yellow')"></div>
                <div class="deviceInput colorBtn lightblue" onclick="send('/led/lightblue')"></div>
                <div class="deviceInput colorBtn hotpink" onclick="send('/led/hotpink')"></div>
            </div>
            <div class="buttonCluster">
                <div class="buttonRow clusterItem">
                    <div class="deviceInput clusterItem" onclick="send('/led/party')">PARTY</div>
                </div>
                <div class="buttonRow clusterItem">
                    <div class="deviceInput clusterItem" onclick="send('/led/smooth')">SMOOTH</div>
                    <div class="deviceInput clusterItem" onclick="send('/led/smoothrgb')">SMOOTH RGB</div>
                </div>
            </div>
        </div>
        <div class="deviceWrapper">
            <h2 class="deviceTitle">Beamer</h2>
            <div class="deviceInput deviceSwitch" onclick="send('/beamer/toggle/')">TOGGLE</div>
        </div>
        <!-- <div class="deviceWrapper">
            <h2 class="deviceTitle">Settings</h2><input type="text" class="ipInput" value=""><a id="espLink"
                target="_blank" href="https://null">Allow everything here [https://null]</a>
            <div class="buttonCluster">
                <div class="buttonRow clusterItem">
                    <div class="deviceInput clusterItem">Theme wechseln</div>
                </div>
            </div>
        </div> -->
    </div>
</body>

</html>
  """
  return html

