# Deep Learning from First Principles 🧠

> "What I cannot create, I do not understand." — Richard Feynman

## 🚀 About The Project
This repository documents my journey building a Neural Network framework from scratch using **only NumPy**. No PyTorch, no TensorFlow, no magic black boxes.

## 🛠️ Tech Stack
* **Python 3.10+**
* **NumPy** (Linear Algebra)

## 📂 Progress Log
| Day | Concept | Status |
| :--- | :--- | :--- |
| **01** | Dense Layer (Forward Pass) | ✅ Completed |
| **02** | Activation Functions (ReLU) | ⏳ Upcoming |
| **03** | Backpropagation | ⏳ Upcoming |

## 💡 Key Learnings (Day 1)
* **Initialization matters:** `0.1 * randn` prevents gradient explosion.
* **Vectorization:** Using `np.dot` is infinitely faster than Python loops.
* **Shapes:** Debugging matrix dimensions `(N, D)` vs `(D, K)` is 90% of the work.

## 💻 How to Run
```bash
# Clone the repo
git clone [https://github.com/Bhanu-teja-VCE/numpy-neural-network.git](https://github.com/Bhanu-teja-VCE/numpy-neural-network.git)

# Install dependencies
pip install numpy

# Run the Day 1 script
python main.py
```
