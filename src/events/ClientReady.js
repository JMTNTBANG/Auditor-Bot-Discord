const { Events } = require("discord.js");

module.exports = {
  name: Events.ClientReady,
  async execute(ctx) {
    console.log(`Logged in as ${ctx.user.tag}`)
  },
};
