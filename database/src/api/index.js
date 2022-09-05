const router = require('express').Router();
const enterprise = require('./routes/enterprise');
const user = require('./routes/user');
const userXEnterprise = require('./routes/userXEnterprise');
const transaction = require('./routes/transaction'); 


router.use('/enterprises', enterprise);
router.use('/users', user);
router.use('/user-x-enterprises', userXEnterprise);
router.use('/transactions', transaction);

module.exports = router;