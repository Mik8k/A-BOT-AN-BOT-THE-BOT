import discord
from discord.ext import commands
from sla_logic import gen_pass
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot= commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')
@bot.command()
async def lixo(ctx):
    await ctx.send("Azul: Papel e papelão Vermelho. Plástico Verde. Vidro Amarelo. Metal Marrom. Resíduos orgânicos restos de alimentos, cascas de frutas Cinza. Resíduos não recicláveis ou misturados Preto. Madeira Laranja. Resíduos perigosos pilhas, baterias, lâmpadas Branco. Resíduos de serviços de saúde hospitais, clínicas Roxo. Resíduos radioativos")
@bot.command()
async def meme(ctx):
    with open('images/011.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
bot.run("put the token")
