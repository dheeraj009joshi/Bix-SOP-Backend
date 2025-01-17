const express = require('express');
const {
  registerUser,
  loginUser,
  getCurrentUser,getUserLeads,
} = require('../../controllers/userController');
const { protect } = require('../../middlewares/authMiddleware');

const router = express.Router();

router.post('/register', registerUser);
router.post('/login', loginUser);
router.get('/me', protect, getCurrentUser);
router.get('/leads', protect, getUserLeads);

module.exports = router;
