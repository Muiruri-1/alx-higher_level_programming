#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);

	printf("[*] first 10 bytes: ");
	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

