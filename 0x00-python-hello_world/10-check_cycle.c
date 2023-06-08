#include "lists.h"
/*
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *xx = list;

	if (!list)
		return (0);

	while (x && xx && xx->next)
	{
		x = x->next;
		xx = xx->next->next;
		if (x == xx)
			return (1);
	}

	return (0);
}
