# adiciona o , render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.jogador import Jogador as jg



#Instanciar o blueprint
jgBp = Blueprint('jgBp', __name__)


@jgBp.route('/jg')
def jg_list():
#    return "Teste"
    #adiciona isso
    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    jgs_query = jg.query.all()
    return render_template('jg_list.html', jgs=jgs_query)


@jgBp.route('/jg/create')
def create_jg():
    return render_template('jg_create.html')


@jgBp.route('/jg/add', methods=["POST"])
def add_jg():

    sNome = request.form["nome"]
    sPosicao = request.form["posicao"]
    sNacionalidade = request.form["nacionalidade"]
    jogador = jg(nome=sNome, posicao=sPosicao, nacionalidade=sNacionalidade)
    db.session.add(jogador)
    db.session.commit()

    return redirect(url_for("jgBp.jg_list"))


@jgBp.route('/jg/update/<jg_id>')
def update_jg(jg_id=0):
    jg_query = jg.query.filter_by(id = jg_id).first()
    return render_template('jg_update.html', jg=jg_query)

@jgBp.route('/jg/upd', methods=["POST"])
def upd_jg():

    ijg = request.form["id"]
    sNome = request.form["nome"]
    sPosicao = request.form["posicao"]
    sNacionalidade = request.form["nacionalidade"]

    jogador = jg.query.filter_by(id = ijg).first()
    jogador.nome = sNome
    jogador.nacionalidade = sNacionalidade
    jogador.posicao = sPosicao
    db.session.add(jogador)
    db.session.commit()

    return redirect(url_for("jgBp.jg_list"))

@jgBp.route('/jg/delete/<jg_id>')
def delete_jg(jg_id=0):
    jg_query = jg.query.filter_by(id = jg_id).first()
    return render_template('jg_delete.html', jg=jg_query)

@jgBp.route('/jg/dlt', methods=["POST"])
def dlt_jg():
    ijg = request.form["id"]
    jogador = jg.query.filter_by(id = ijg).first()
    db.session.delete(jogador)
    db.session.commit()
    return redirect(url_for("jgBp.jg_list"))