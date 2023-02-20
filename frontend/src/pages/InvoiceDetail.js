import {useState, useEffect} from "react";
import {useParams} from "react-router-dom";

const InvoiceDetail = () => {
    const id = useParams().id
    let [invoice, setInvoice] = useState(() => {
        return {}
    })

    useEffect(() => {
        getInvoice()
    }, [])

    let getInvoice = async () => {
        let invoice = await fetch(`/invoices/${id}/`)
        let invoice_data = await invoice.json()
        setInvoice(invoice_data)
    }

    return (
            <div className="invoice">
                <p>{invoice.document_nr}</p>
            </div>
    )
}


export default InvoiceDetail
