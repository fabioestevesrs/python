import './App.css';
import {useState, useEffect} from "react";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.css'
import JogadorList from "./components/JogadorList";

function App() {
  const [jogadorList, setJogadorList] = useState([{}])
  const [jogadorNome, setJogadorNome] = useState('')
  const [jogadorIdade, setJogadorIdade] = useState('')
  const [jogadorTime, setJogadorTime] = useState('')
  const url = 'http://127.0.0.1:8000'

  useEffect(() => {
    axios.get(`${url}/jogadores`)
      .then(resposta => {
        setJogadorList(resposta.data)
      })
      .catch(error => {
          console.log(error)
        }
      )
  }, []);

  const adicionarJogador = () => {
    const jogador = {
      'nome': jogadorNome,
      'idade': jogadorIdade,
      'time': jogadorTime
    }

    axios.post(`${url}/jogadores`, jogador)
      .then(resposta => {
        console.log('post ok')
        console.log(resposta)
      })
      .catch(error => {
        console.log('post deu ruim')
        console.log(error)
      })
  }

  return (
    <div className='container'>
      <div className='mt-3 justify-content-center align-items-center mx-auto'
           style={{"width": "60vw", "backgroundColor": "#ffffff"}}>
        <h2 className='text-center text-white bg-success card mb-1'>Gerenciamento de Jogadores</h2>
        {/*<h6 className='card text-center text-white bg-success mb-2 pb-2'>Informações do Jogador</h6>*/}
        <div className='card-body text-center'>
          <h5 className='card text-center text-white bg-dark mb-2 pb-1'>Cadastro</h5>
          <span className='card-text'>
            <input onChange={event => setJogadorNome(event.target.value)}
                   className='mb-2 form-control' placeholder='Informe o nome'/>
            <input onChange={event => setJogadorIdade(event.target.value)}
                   className='mb-2 form-control' placeholder='Informe a idade'/>
            <input onChange={event => setJogadorTime(event.target.value)}
                   className='mb-2 form-control' placeholder='Informe o time'/>
            <button onClick={event => adicionarJogador()}
                    className='btn btn-outline-success mb-4'>Cadastrar</button>
          </span>
          <h5 className='card text-center text-white bg-dark mb-4 pb-1'>Lista de Jogadores</h5>
          <div>
            <JogadorList jogadorList={jogadorList}/>
          </div>
        </div>
        <h6 className='card text-center text-light bg-success py-1'>&copy; Rodapé</h6>
      </div>
    </div>
  );
}

export default App;
