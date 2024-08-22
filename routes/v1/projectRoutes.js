const express = require('express');
const {
  createProject,
  getProjects,
  getProject,
  updateProject,
  deleteProject,
  updateCheckpoint,
} = require('../../controllers/projectController');
const { protect } = require('../../middlewares/authMiddleware');

const router = express.Router();

router.route('/')
  .get(protect, getProjects)
  .post(protect, createProject);

router.route('/:id')
  .get(protect, getProject)
  .put(protect, updateProject)
  .delete(protect, deleteProject);

router.route('/:projectId/checkpoint/:checkpointIndex')
  .patch(protect, updateCheckpoint)

module.exports = router;
