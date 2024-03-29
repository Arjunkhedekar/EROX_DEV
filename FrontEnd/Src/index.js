const express = require("express");
const app = express();
const path = require("path");
const port = 8080;
const { Storage } = require('@google-cloud/storage');
const Multer = require('multer');
const src = path.join(__dirname,"views")

app.use(express.static(src));

const multer = Multer({
    storage: Multer.memoryStorage(),
    limits: {
        fileSize: 5 * 1024 * 1024 // it means till 5 mb 
    }
})

let projectId='qwiklabs-gcp-01-fbc3030445d6';
let keyFilename='mykey.json';

const storage = new  Storage({
    projectId,
    keyFilename
});
const bucket = storage.bucket(' ')
app.get('/upload',async (req,res) => {
    const [files] = await bucket.getFiles();

    res.send([files])
})

app.post('/upload' , multer.single('imgfile'),(req,res) =>{
    console.log('Made it/upload')
    try{
        if(req.file){
            console.log('File found, trying to upload...')
            const blob = bucket.file(req.file.originalname);
            const blobStream = blob.createWriteStream();

            blobStream.on('finish',() =>{
                res.status(200).send('Success');
                console.log('Success');
            })
            blobStream.end(req.file.buffer);
        }else throw "error with img";
    }catch(error){
        res.status(500).send(error)
    }
})

app.get('/', (req,res) => {
    res.sendFile(src + '/index.html');
})

app.listen(port, () => {
    console.log('Server started on port ${port}');
});
