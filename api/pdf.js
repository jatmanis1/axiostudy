export default async function handler(req, res) {
    // URL of the original PDF file you want to render
    const pdfUrl = "https://p-def6.pcloud.com/DLZfQM0KGZWajDmS7ZlduM7ZZc8whXkZ1ZZcu8ZZsjEJZI4ZjYZqpZJPf0Lt7KNdBcBFHjcbniXprzgsgy/Week_1.pdf";

    try {
        // Fetch the PDF file
        const response = await fetch(pdfUrl);

        if (!response.ok) {
            res.status(500).send("Failed to fetch PDF");
            return;
        }

        // Set CORS headers to allow cross-origin access
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Content-Type", "application/pdf");

        // Send the PDF file content as the response
        res.send(await response.buffer());
    } catch (error) {
        res.status(500).send("Error fetching PDF: " + error.message);
    }
}
