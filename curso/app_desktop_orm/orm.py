from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, primary_key=False)
    ano = Column(Integer, primary_key=False)
    nota = Column(Float, primary_key=False)


engine = create_engine("sqlite:///banco.db", echo=True)
Base.metadata.create_all(engine)


def adicionar(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)

    session.add(filme)
    session.commit()
    session.close()


def atualizar(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()

    if filme:
        filme.nome = nome if nome is not None else filme.nome
        filme.ano = ano if ano is not None else filme.ano
        filme.nota = nota if nota is not None else filme.nota

    session.commit()
    session.close()


def excluir(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()

    if filme:
        session.delete(filme)

    session.commit()
    session.close()

# adicionar('Mario', 2020, 8.5)
#
# adicionar('Interestelar', 2011, 9.5)

# atualizar(1, "Mario", None, 8.5)

# excluir(1)
