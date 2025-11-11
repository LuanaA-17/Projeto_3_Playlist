import streamlit as st 

generos ={
    'Pop' : {
        'The Weeknd' : 'https://youtu.be/YQ-qToZUybM?si=LI-RKhLk0pAEP1XT',
        'Justin Timberlake' : 'https://youtu.be/3LmSjmcUNh8?si=SjcEWDi062NioheT',
        '50 Cent' : 'https://youtu.be/5RDSkR8_AQ0?si=sJQPeGjWISSqfY95'
    },
    'Rock' : {
        'Charlie Brown JR' : 'https://youtu.be/i4FQJ7Qi14o?si=eSr8ku-gvTj_dLzN',
        'Bon Jovi' : 'https://youtu.be/lDK9QqIzhwk?si=R9U0gDLAdbhFft_2'
    },
    'Rap' : {
        'Racionais' : 'https://youtu.be/Wb3rvC6z5ao?si=0gqxfEGRjWKFl7kp',
        'Hungria' : 'https://youtu.be/pdFLuRQd0wQ?si=n8jFY-QUk69xRPh6'
    },
    'Pagode' : {
        'Alexandre Pires' : 'https://youtu.be/NsPZN35M8SQ?si=kE4qnGQYDdj5higX',
        'Grupo Menos é Mais' : 'https://youtu.be/dnD5TQAI2b0?si=-r38SyCvS1s85rGE'
    },
}

st.sidebar.title('Lunas Cat') 
st.sidebar.image('gato.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())
st.title(artista)
video, sobre = st.tabs(['Vídeo', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'The Weeknd':
        st.markdown('Abel Makkonen Tesfaye, mais conhecido por seu nome artístico The Weeknd, é um cantor, compositor, ator e produtor musical canadense.' \
        'Conhecido por sua versatilidade sonora e lirismo sombrio, suas músicas exploram temas de escapismo, romance e melancolia, e são frequentemente inspiradas em experiências pessoais ')

    elif artista == 'Justin Timberlake':
        st.markdown('Justin Randall Timberlake é um cantor, compositor, ator, produtor musical, dançarino, multi-instrumentista e empresário norte-americano.' \
        ' Ex-integrante da boy band N Sync, Timberlake lançou em 2002 seu primeiro álbum em carreira solo, Justified, que vendeu mais de sete milhões de cópias mundialmente')
    
    elif artista == '50 Cent':
        st.markdown('Curtis James Jackson III, mais conhecido pelo seu nome artístico 50 Cent, é um rapper, compositor, ator, diretor, roteirista e empresário norte-americano.' \
        ' Ficou conhecido com o lançamento dos álbuns Get Rich or Die Tryin e The Massacre.')

    elif artista == 'Charlie Brown JR':
        st.markdown('Charlie Brown Jr. foi uma banda de rock brasileira formada em Santos, em 1992, tendo em sua formação original o vocalista Chorão, o baixista Champignon, os guitarristas Marcão Britto e Thiago Castanho, além do baterista Renato Pelado.')

    elif artista == 'Bon Jovi':
        st.markdown('Bon Jovi é uma banda americana de rock, formada em 1983, em Sayreville, Nova Jersey.' \
        'A formação atual da banda consiste no cantor Jon Bon Jovi, no tecladista David Bryan, no baterista Tico Torres, no guitarrista Phil X e no baixista Hugh McDonald.')

    elif artista == 'Racionais':
        st.markdown('Racionais, é um grupo brasileiro de rap fundado em 1988 na cidade de São Paulo.' \
        'É formado por Pedro Paulo Soares Pereira, Paulo Eduardo Salvador, Edivaldo Pereira Alves e Kleber Geraldo Lelis Simões.' \
        ' É o maior grupo de rap do Brasil, e está entre os grupos musicais mais influentes do país e da música brasileira')

    elif artista == 'Hungria':
        st.markdown('Gustavo da Hungria Neves é um rapper, cantor, compositor e empresário brasileiro.' \
        ' Hungria ficou conhecido nacionalmente pelo seu primeiro single, "Bens Materiais", mas só alcançou sucesso fora')

    elif artista == 'Alexandre Pires':
        st.markdown('Alexandre Pires do Nascimento é um cantor, compositor e multi-instrumentista brasileiro.' \
        ' Em 1989, fundou o grupo de pagode romântico Só Pra Contrariar, sendo o vocalista principal até a sua saída no início dos anos 2000.')

    elif artista == 'Grupo Menos é Mais':
        st.markdown('Menos É Mais é um grupo brasileiro de pagode formado em 2016 na cidade do Gama no Distrito Federal por Duzão, Gustavo Goes, Paulinho Félix e Ramon Alvarenga.' \
        ' O grupo ganhou notoriedade por regravar faixas antigas de sucesso de outros cantores.')

        
    