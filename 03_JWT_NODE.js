// RUNNING node 03_JWT_NODE.js 

const express = require('express')
const jwt = require('jsonwebtoken')

const app = express()

const PORT = process.env.PORT || 3000;
app.use(express.json())

SECRET_KEY_APP = "25a2aaaed449c7d3125c9fd6d3131e109f6531f35db1c519b4c1ee6a3352dc85"

// mock user data 
const users = [
    {id: 1, 'username': "jaka prima maulana", "password": "admin@1234"}
]

app.post('/login', (req, res) => {
    const {username, password} = req.body;
    const userInstance = users.find(user_data => user_data.username === username && user_data.password === password);

    if (userInstance) {
        const token = jwt.sign({id: userInstance.id, username: userInstance.username}, SECRET_KEY_APP, {expiresIn: '1h'})
        res.json({token})
    } else {
        res.status(401).json({message: 'Invalid username or password'})
    }
});

app.get('/protected', authenticateToken, (req, res, next) => {
    res.json({message: 'Protected route accessed successfully'})
})

// middleware
function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (token == null) {
        return res.sendStatus(401)
    }

    jwt.verify(token, SECRET_KEY_APP, (err, user) => {
        if (err) {
            return res.sendStatus(403);
        }
        req.user = user;
        next();
    })
}

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`)
})