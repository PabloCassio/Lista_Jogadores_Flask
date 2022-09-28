from ..extensions import db

class Jogador(db.Model):
    __tablename__ = "jogadores_favoritos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    posicao = db.Column(db.String(50))
    nacionalidade = db.Column(db.String(500))
    def __repr__(self):
        return "<Jogador(nome={}, posicao={}, nacionalidade={})>".format(self.nome, self.posicao, self.nacionalidade)