import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import InvoiceList from "./pages/InvoiceList";

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="" exact element={<InvoiceList/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;
