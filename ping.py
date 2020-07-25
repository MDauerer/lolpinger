from pythonping import ping


COLORS = {
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

response_list = ping('104.160.141.3', size = 40, count = 20)

def colorize(ping):
    if float(ping) < 50:
        return "green"
    elif float(ping) > 50 and float(ping) < 100:
        return "yellow"
    else:
        return "red"


#average ping
avg_ping = float(response_list.rtt_avg_ms)
avg_print = colorText("Your average Ping to LOL EUW is: " + "[[" + colorize(avg_ping) + "]]" + str(avg_ping) + "[[white]]")

#maxp ping
max_ping = float(response_list.rtt_max_ms)
max_print = colorText("Your maximum Ping to LOL EUW is: " + "[[" + colorize(max_ping) + "]]" + str(max_ping) + "[[white]]")

#lowest ping
min_ping = float(response_list.rtt_min_ms)
min_print = colorText("Your minimum Ping to LOL EUW is: " + "[[" + colorize(min_ping) + "]]" + str(min_ping) + "[[white]]")





print("Your average ping to LOL EUW is: " + avg_print + " ms"))
print("Your highest ping to LOL EUW is: " + max_print + " ms")
print("Your lowest ping to LOL EUW is: " + min_print + " ms")


wait = input ('Press Enter to continue')


