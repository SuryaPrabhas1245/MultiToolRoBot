Bot.sendMessage("Writing Notes...\nIt may take 2-4 seconds")
Api.sendPhoto({
  photo:
    "https://cahhwaala.herokuapp.com/mia?text=" +
    message +
    "",
  caption: "Note Written By *@" + bot.name + "*",
  parse_mode: "Markdown"
})
