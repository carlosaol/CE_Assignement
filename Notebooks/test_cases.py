import unittest
import numpy as np
from IPython.display import Markdown, display

import __main__

global test_func

class test_init_layer(unittest.TestCase):
    
    def test_return(self):
        ret = test_func(2,3)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")
        
    def test_shape(self):
        l1=np.random.randint(10)
        l2=np.random.randint(10)
        w,b= test_func(l1,l2)
        self.assertEqual(w.shape,(l2,l1),msg ='the weights shape is incorrect')
        self.assertEqual(b.shape,(l2,1),msg ='the weights shape is incorrect')

    def test_distribution(self):
        w,b=test_func(4,6)
        self.assertLessEqual(abs(w.mean()),1 , msg = "mean of the weights should be less than one")
        self.assertLessEqual(abs(b.mean()),1 , msg =  "mean  of the bias should be less or equal than one")

        self.assertNotEqual(w.std(),0 , msg = "all your vales are equal")
        self.assertNotEqual(b.std(),0 , msg = "all your vales are equal")

class test_preactivation(unittest.TestCase):
    def get_random_weights(self):
        l1=np.random.randint(3,10)
        l2=np.random.randint(3,10)
        w= np.random.randint(10,size=(l2,l1))
        b= np.random.randint(10,size=(l2,1))
        x= np.random.randint(10,size=(l1,1))

        return w,b,x
    
    def test_return(self):
        w,b,x = self.get_random_weights()
        ret = test_func(w,b,x)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")

    def test_shape(self):
        w,b,x = self.get_random_weights()
        z = test_func(w,b,x)
        self.assertEqual(z.shape,(len(b),1),msg ='the activation output shape is incorrect, review the matrix order')

    def test_known_values(self):
        w = np.array([[2,4],[3,5]])
        b = np.array([[0],[-6]])
        x= np.array([[2],[4]])
        z = test_func(w,b,x)
        expected =np.array([[20],[20]])
        is_equal = np.equal(z,expected).all()
        self.assertEqual(is_equal,True, msg ='result is not correct, review the equations')

    def test_random_values(self):
        w,b,x = self.get_random_weights()
        z = test_func(w,b,x)
        expected = np.dot(w,x)+b
        is_close = np.isclose(z,expected).all()
        self.assertEqual(is_close,True, msg ='result is not correct, review the equations')


class test_relu(unittest.TestCase): 
    def test_return(self):
        ret = test_func(10)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")
        
    def test_positive(self):
        ret = test_func(10)
        self.assertEqual(ret,10, msg = 'the output is incorrect for positive values')
        eps = 0.0001
        ret = test_func(eps)
        self.assertEqual(ret,eps, msg = 'the output is incorrect for small positive values')
        x = np.inf
        ret = test_func(x)
        self.assertEqual(ret,x, msg = 'the output is incorrect for large positive values')

    def test_negative(self):
        ret = test_func(-10)
        self.assertEqual(ret,0, msg = 'the output is incorrect for negative values')
        eps = -0.0001
        ret = test_func(eps)
        self.assertEqual(ret,0, msg = 'the output is incorrect for small negative values')
        x = -np.inf
        ret = test_func(x)
        self.assertEqual(ret,0, msg = 'the output is incorrect for large negative values')

class test_relu_prime(unittest.TestCase):  
    def test_return(self):
        ret = test_func(10)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")
        
    def test_positive(self):
        ret = test_func(10)
        self.assertEqual(ret,1, msg = 'the output is incorrect for positive values')
        eps = 0.0001
        ret = test_func(eps)
        self.assertEqual(ret,1, msg = 'the output is incorrect for small positive values')
        x = np.inf
        ret = test_func(x)
        self.assertEqual(ret,1, msg = 'the output is incorrect for large positive values')

    def test_negative(self):
        ret = test_func(-10)
        self.assertEqual(ret,0, msg = 'the output is incorrect')
        eps = -0.0001
        ret = test_func(eps)
        self.assertEqual(ret,0, msg = 'the output is incorrect')
        x = -np.inf
        ret = test_func(x)
        self.assertEqual(ret,0, msg = 'the output is incorrect for large negative values')

class test_sigmoid(unittest.TestCase): 
    def test_return(self):
        ret = test_func(10)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")
        
    def test_positive(self):
        ret = test_func(0)
        self.assertEqual(ret,0.5, msg = 'the output is incorrect')
        ret = test_func(np.log(2))
        self.assertAlmostEqual(ret,2/3, places = 4, msg= 'the output is incorrect for  positive values')
        x = np.inf
        ret = test_func(x)
        self.assertEqual(ret,1, msg = 'the output is incorrect for large positive values')

    def test_negative(self):
        ret = test_func(-np.log(2))
        self.assertAlmostEqual(ret,1/3, places=4, msg= 'the output is incorrect for negative values')
        ret = test_func(-np.log(4))
        self.assertAlmostEqual(ret,1/5, places=4, msg= 'the output is incorrect for negative values')
        x = -np.inf
        ret = test_func(x)
        self.assertEqual(ret,0, msg = 'the output is incorrect for large negative values')

class test_sigmoid_prime(unittest.TestCase):   
    def test_return(self):
        ret =  test_func(10)
        self.assertIsNotNone(ret,msg = "fuction doesn't return anything")
        
    def test_positive(self):
        ret =  test_func(0)
        self.assertEqual(ret,0.25, msg = 'the output is incorrect for positive values')
        ret =  test_func(np.log(2))
        self.assertAlmostEqual(ret,2/9, places=4, msg= 'the output is incorrect for positive values')
        x = np.inf
        ret = test_func(x)
        self.assertEqual(ret,0, msg = 'the output is incorrect for large positive values')

    def test_negative(self):
        ret =  test_func(-np.log(2))
        self.assertAlmostEqual(ret,2/9 , places=4, msg= 'the output is incorrect for negative values')
        ret =  test_func(-np.log(4))
        self.assertAlmostEqual(ret,4/25, places=4, msg= 'the output is incorrect for negative values')
        x = -np.inf
        ret = test_func(x)
        self.assertEqual(ret,0, msg = 'the output is incorrect for large negative values')

Tests={ 'test_init_layer'    : test_init_layer,
        'test_preactivation' : test_preactivation,
        'test_relu'          : test_relu,
        'test_relu_prime'    : test_relu_prime,
        'test_sigmoid'       : test_sigmoid,
        'test_sigmoid_prime' : test_sigmoid_prime}

def printmd(string):
    display(Markdown(string))

def run_check(check_name, func):
    global test_func

    check = Tests[check_name]
    test_func = func
    results = unittest.main(module=check(),argv=[''], verbosity=2, exit=False)

    if(results.result.wasSuccessful()):
        printmd('**<span style="color: green;">PASSED</span>**')
    else:
        printmd('**<span style="color: red;">FAILED</span>**')

    return results.result
    