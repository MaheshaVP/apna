import Title from './Title';
import './App.css'


function Para() {
  return <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. In, aliquid?</p>
}

function Btn () {
  return <button>Hit me</button>
}

function App() {
  return(
    <div>
      <h1>Good morning</h1>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo fugiat maiores a eveniet placeat fugit aliquid eum officia sunt iusto!</p>
      <button>click me</button>
      
      <Btn/>

      <Title/>
      <Para/>
      <Title/>
      <Para/>

    </div>
  );
}

export default App
