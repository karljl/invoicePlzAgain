import {useState, useEffect} from "react";

const InvoiceList = () => {
    let [invoices, setInvoices] = useState(() => {
        return []
    })

    useEffect(() => {
        getInvoices()
    }, [])

    let getInvoices = async () => {
        let invoices = await fetch("/invoices/")
        let invoices_data = await invoices.json()
        setInvoices(invoices_data)
    }

    return (
        <>
            <div className="invoice-list">
                {invoices.map(invoice => (
                    <p>{invoice.document_nr} by {invoice.provider}</p>
                ))}
            </div>
        </>
    )
}


export default InvoiceList
