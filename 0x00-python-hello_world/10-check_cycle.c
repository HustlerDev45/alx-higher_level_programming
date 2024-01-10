#include "lists.h"

/**
 * check_cycle - Checks if it contains a cycle.
 * @list: Pointer to the haed of the list.
 *
 * Return: 0 if no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
