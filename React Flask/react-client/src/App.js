import { useState } from "react"
import Index from './components/IndexPage/Index'

function App() {
    const [fontData,setFontData] = useState([1,2,3,4,5,6,7])
    // const getData = async () => {
    //   try{
    //     const data = await fetch("/")
    //     console.log(data)
    //     setFontData(data)
    //   }catch(err){
    //     console.log(err)
    //   }
    // }
    // getData()
    const result = fontData.map((item,index) => <p key={index}>{item}</p>)


  return (
    <div className="App">
      <h1 className="header">What fonts?</h1>
      <Index/>
      <div className="font-detial">
        <h2 className="font-detial-head">Font detials:</h2>
        <div className="font-detial-body">
          <h4>Font Name: <span>ITC Avant Garde Gothic W01 Bd.</span></h4>
          <h4>Publisher Name: <span>http://www.monotype.com.</span></h4>
          {result}
        </div>
      </div>
    </div>
  );
}

export default App;
