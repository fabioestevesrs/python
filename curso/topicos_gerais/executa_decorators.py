from modulos_decorator import to_upper, split_name


@split_name
@to_upper
def meu_nome() -> str:
    return 'Fábio baiano'


print(meu_nome())
