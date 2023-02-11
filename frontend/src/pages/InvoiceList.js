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
                    <p>Invoice</p>
                ))}
            </div>
        </>
    )
}


export default InvoiceList
