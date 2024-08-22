const mongoose = require('mongoose');

const Project = new mongoose.Schema({
  title: { type: String, required: true, trim: true },
  description: { type: String, required: true, trim: true, lowercase: true, unique: true },
  addedBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  checkpoints: [{
    text: { type: String},
    completed: { type: Boolean, default: false },
    completedBy: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  }],
}, { timestamps: true });

module.exports = mongoose.model('Project', Project);
