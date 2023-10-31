#include "lists.h"

/**
 * check_cycle - singly linked list
 * @list: linked list
 *
 * Return: true or false
 */
 
int check_cycle(listint_t *list)
{
	listint_t *curr = list->next;
	while (curr->next != NULL && curr->next != list)
		curr = curr->next;
	if (curr->next == NULL)
		return 0;
	else
		return 1;
}
