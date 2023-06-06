#include "lists.h"

/**
 * check_cycle -  function that checks if has a cycle in it.
 * @list: header list pointer
 * Return: 0 or 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *x;

	if (list == NULL || list->next == NULL)
		return (0);
	x = list;
	while (x && x->next)
	{
		list = list->next;
		x = (x->next)->next;
		if (list == x)
			return (1);
	}
	return (0);
}
