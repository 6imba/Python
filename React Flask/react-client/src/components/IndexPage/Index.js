import './Index.css'

const Index = () => {
    const enterPressed = (e) => {
        if(e.target.value==""){
            alert("Empty url not allowed!!!")
        }
        if(e.keyCode === 13){
            alert("Enter key pressed!!!")
            alert("Redirect to the python script event handler function!!!")
        }
    }   

    return (
        <div className="url-search">
            <span className="inputfield-head">Enter url of the font file:</span>
            <input type="text" placeholder="uniform resources locator..." className="inputbox" onKeyUp={enterPressed}></input>
        </div>
    )
}

export default Index