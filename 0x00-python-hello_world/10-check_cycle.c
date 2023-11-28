#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 * @list: Pointer to the head of the list.
 *
 * Return: 0 if no cycle, 1 if there is a cycle.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

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
