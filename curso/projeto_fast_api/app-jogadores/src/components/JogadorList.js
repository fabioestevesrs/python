import React from "react";
import Jogador from "./Jogador";

function JogadorList(props) {
  return (
    <div>
      <ul>
        {
          props.jogadorList.map(
            (jogador, indice) => {
              return (<Jogador jogador={jogador} key={indice}/>)
            }
          )
        }
      </ul>
    </div>
  )
}

export default JogadorList;