from uagents import Agent, Context

alice = Agent(name='alice', seed='12345')
# print(f'{alice.address=}')  # agent address
# print(f'{alice.wallet.address()=}')  # fetch network address


@alice.on_event('startup')
async def say_hello(ctx: Context):
  ctx.logger.info(f'hello, my name is {ctx.name}')

alice.run()
