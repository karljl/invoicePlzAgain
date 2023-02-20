import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import InvoiceList from "./pages/InvoiceList";
import InvoiceDetail from "./pages/InvoiceDetail";

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="invoices/" exact element={<InvoiceList/>}/>
                    <Route path="invoices/:id/" element={<InvoiceDetail/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;
