

import React, { Component } from 'react'

const SERVER_PREFIX = "http://127.0.0.1:5000/";

export default class Board extends Component {
  constructor(props){
    super(props);
    this.state = {squares: []}
  }

  async componentDidMount() {
    const response = await fetch(SERVER_PREFIX + 'start_game');
    const board = await response.json();
    this.setState({squares: this.renderSquares(board)}, (squares) => console.log(squares));
  }

  renderSquares(board){
      console.log(board.flat());
      return (board.flat()).map((val,i)=>this.renderSquare(val, i));
  }

  renderSquare(player, id){
    return (<button 
          id={`sq${id+1}`} 
          onClick={()=> player === '#' ? this.playerMove(id) : null}>
            {player === '#' ? "" : player }
        </button>);
  }

  async aiMove(){
    this.updateBoard('ai_move');
  }

  async playerMove(index){

    const response = await fetch(SERVER_PREFIX + 'player_move', {
    headers: {
      'Content-Type': 'application/json'
    },
      method: 'POST', body: JSON.stringify({index: index})
    });
    // const response = await fetch(SERVER_PREFIX + 'player_move', {
    //   method: 'POST',
    //   body: {row: r, col: c}
    // });
    const board = await response.json();
    this.setState({squares: this.renderSquares(board)}, (squares) => {console.log(squares); 
      this.updateBoard('ai_move');
    });
  }

  async updateBoard(reqStr){
    const response = await fetch(SERVER_PREFIX + reqStr);
    const board = await response.json();
    this.setState({squares: this.renderSquares(board)}, (squares) => console.log(squares));
  }

  render(){
    return (
      <div className="board-wrapper">
          <div className="board-ttt">{this.state.squares}</div>
      </div>
  );
  }
}