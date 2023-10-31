#include "lists.h"

/**
 * check_cycle - singly linked list
 * @list: linked list
 *
 * Return: true or false
 */
int check_cycle(listint_t *list)
{
	listint_t *itr1, *itr2;

	if (!list)
		return (0);
	itr1 = list, itr2 = list->next;
	while (itr2 != NULL && itr2->next != NULL)
	{
		itr1 = itr1->next;
		itr2 = itr2->next->next;
		if (itr2 == itr1 ||itr2 == itr1->next)
			return (1);
	}
	return (0);
}
