const { Events } = require('discord.js');

module.exports = {
    name: Events.InteractionCreate,
    async execute(ctx) {
        if (!ctx.isChatInputCommand()) return;
        const command = ctx.client.commands.get(ctx.commandName);
        await command.execute(ctx);
    }
}