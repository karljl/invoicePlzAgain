import {useState, useEffect} from "react";

const InvoiceList = () => {
    let [invoices, setInvoices] = useState(() => {
        return []
    })

    useEffect(() => {
        getInvoices()
    }, [])

    let getInvoices = async () => {
        let response = await fetch("invoices/")
        let data = await response.json()
        setInvoices(data)
    }

    return (
        <>
            <div className="invoice-list">
                {invoices.map(invoice => (
                    <ul key={invoice.id}>
                       <li>ID: {invoice.id}</li>
                       <li>Document nr: {invoice.document_nr}</li>
                       <li>Created: {invoice.created}</li>
                       <li>Rows: {invoice.invoice_rows.map(
                           invoice_row => (<p>row</p>)
                       )}</li>
                    </ul>
                ))}
            </div>
        </>
    )
}


export default InvoiceList
