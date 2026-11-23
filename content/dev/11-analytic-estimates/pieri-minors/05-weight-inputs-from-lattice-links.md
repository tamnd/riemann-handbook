---
title: Weight inputs from lattice links
decls:
  - Formalism.CohomologicalDescent.FrobeniusPeriodChange.weight_exponents_from_lattice
  - Formalism.CohomologicalDescent.WorkedExample.orientation_lattice_holds
  - Formalism.CohomologicalDescent.ShortWeightBounds.depth_of_linkage_holds
  - Formalism.CohomologicalDescent.ShortWeightBounds.first_input_of_link
  - Formalism.CohomologicalDescent.ShortWeightBounds.weight_inputs_of_linkage_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weight inputs from lattice links

This section proves the depth bound that the [lattice inclusions](/entry/down7-inclusion-w-seven-real-holds/) of Section 4 take as an input. There, the weight inputs at a prime $l$ ask that every relevant highest weight $w$ of a thick index $\tau$ has depth $d_{\varpi_{k_c + j_\tau}}(\lambda_\tau|_{N_r}, w)$ at most the depth budget $i_\tau(l)$. Here we replace this condition by a *lattice link*: a family of lattices over a power series ring, with a Frobenius matrix and a second matrix of an action, whose elementary divisors are the shifted entries of $w$. The final result, the weight inputs from lattice links, feeds the [inclusion of models](/entry/l-incl-of-models/).

**Definition 4.5.1 (Labels).** Let $E$ be a finite set and $N \in \mathbb{N}$. A *label system* $D$ on $E$ of length $N$ consists of a map $c : E \to E$, a subset $\Phi \subseteq E$, two families $U_i, U'_i \in \mathbb{Z}^N$ and integers $b_i$ for $i \in E$. Let $\sigma$ be a permutation of $E$ and $h, t \in \mathbb{N}$. Write $\bar a = N - 1 - a$.

1. $D$ is *reflexive* for $(\sigma, h, t)$ if $c$ is an involution that commutes with $\sigma$, every $i$ has $i \in \Phi$ or $c(i) \in \Phi$, and for all $i$ and $a$: $U_{c(i)}(a) = h - U_i(\bar a)$, $U'_{c(i)}(a) = h - U'_i(\bar a)$ and $b_{c(i)} = h - (b_i + t - 1)$.
2. Let $F$ be a field and $\gamma : E \to \mathbb{Z}$. $D$ is *linked* over $F$ for $(t, \gamma)$ if for every $i \in \Phi$: $U_i$ and $U'_i$ are strictly decreasing, each $b_i + s$ with $s < t$ is a value of $U_i$, and $\prod_a (X + U_i(a) + \gamma_i) = \prod_a (X + U'_i(a) + \gamma_i)$ in $F[X]$.
3. Let $\varepsilon : E \to E$, $J_i \in \mathbb{Z}^N$ and $b^J_i \in \mathbb{Z}$. $D$ *carries* $(\varepsilon, J, b^J)$ if $\varepsilon = \mathrm{id}$ or $\varepsilon = c$, and $J_{\varepsilon(i)} = U'_i$ and $b^J_{\varepsilon(i)} = b_i$ for all $i$.

For a prime $l$, $b \in \mathbb{Z}$, $t, \kappa \in \mathbb{N}$ and a finite set $S \subseteq \mathbb{Z}$, let $m_l(b, t, \kappa; S)$ be the number of $u \in S$ with $u \notin [b, b + t - 1]$ that are congruent modulo $l$ to some $x \in [b - \kappa, b + t - 1 + \kappa]$. Put $m_i = m_l(b_i, t, \lfloor h/(l-1) \rfloor; U_i(\{0, \dots, N-1\}))$. Let $N = k + j + t + q$. The label system has *block shape* at $\tau$ if $U_\tau \geq 0$, $\sum_a U_\tau(a) = \sum_a U'_\tau(a)$, and $U_\tau(a) = b_\tau + (k + j + t - 1 - a)$ for $k + j \leq a < k + j + t$. It satisfies the *depth bound* at $\tau$ if
$$\sum_{a < k + j} \bigl(U_\tau(a) - U'_\tau(a)\bigr) \leq q h + \bigl(l\, m_{\sigma(\tau)} + m_\tau\bigr)\bigl(t + 2 \lfloor h/(l-1) \rfloor\bigr).$$

The number $m_i$ is the count $m_\tau(l)$ of Section 4.

**Definition 4.5.2 (Frobenius lattices).** Let $l$ be a prime and $O$ a domain that is a $\mathbb{Z}_l$-algebra. A *lattice family* of rank $n$ on $E$ consists of matrices $P_i, D_i \in M_n(O[[X]])$ and $\Theta_i \in M_n(O)$ for $i \in E$. For $h \in \mathbb{N}$, $u \in \mathbb{Z}_l^\times$ and $U'_i \in \mathbb{Z}^n$, the family is *of weights $U'$* if for every $i$:

1. $P_i M = (X - l)^h \cdot 1$ for some $M \in M_n(O[[X]])$;
2. if every sum of $r$ entries of $U'_i$ is at least $S$, then $(X - l)^S$ divides every $r \times r$ minor of $P_i$;
3. $\det P_i = v\,(X - l)^{\sum_a U'_i(a)}$ for a unit $v$ of $O[[X]]$;
4. $X - l$ divides every entry of $D_i - \Theta_i$;
5. there are $r_a \in \mathbb{Z}_l$ with $u^{-U'_i(a)} = 1 + l r_a$ and $\det(X - \Theta_i) = \prod_a (X - r_a)$.

Let $F$ be a field of characteristic $l$ and $t \in \mathbb{N}$. A *Frobenius datum* $W$ consists of a homomorphism $O \to F$, a series $\mathrm{un} \in O[[X]]$, a lattice family $N$ of rank $n$, lattice families $N^\psi_s$ of rank $1$ for $s < t$, invertible matrices $g_i$ over $F[[X]]$, a block map $\beta : \{0, \dots, n-1\} \to \mathbb{N}$, positions $\mathrm{pos} : \{0, \dots, t-1\} \to \{0, \dots, n-1\}$ and units $w_i(s)$ of $F[[X]]$. From $g_i$, $g_{\sigma(i)}$ and the reductions of $P_i$ and $D_i$ one forms matrices $\Phi_i$ and $\Gamma_i$ over $F[[X]]$. Let $c \in \mathbb{Z}_l$, $\mathrm{wt}, \kappa : E \times \{0, \dots, t-1\} \to \mathbb{Z}$, an ideal $I$ of $O$ with $O$ complete for $I$, a field $L$, $\zeta \in O$, a ring map $e : O \to L$ and ring maps $j_b : O[[X]] \to L[[X]]$. The *lattice inputs* are:

1. the *frame*: $u = 1 + lc$ with $c$ a unit; a unit condition on $\mathrm{un}$; $0 \leq U'_i(a) \leq h$ and $0 \leq \mathrm{wt}_i(s) \leq h$; $\mathrm{pos}$ is injective and $\mathrm{pos}(s)$ is alone in its block; $\Phi_i$ and $\Gamma_i$ are block triangular for $\beta$; and two identities in $F((X))$ that tie the diagonal entries at $\mathrm{pos}(s)$ to $N^\psi_s$, $w_i(s)$ and the powers $X^{\kappa_i(s)}$, $X^{l \kappa_{\sigma(i)}(s)}$;
2. $\zeta$ is a primitive $l$-th root of unity with $\zeta - 1 \in I$, $e$ is injective, and for $0 < b < l$ the map $j_b$ extends $e$ on constants, sends $X - (\zeta^b - 1)$ to $X$ times a unit, and turns the action of $u$ into the rescaling of $X$ by $e(u)$;
3. for $N$ with weights $U'$ and for each $N^\psi_s$ with weights $\mathrm{wt}_\cdot(s)$: an inverse up to a power of a fixed series, condition 4 above, and for $0 < b < l$ a Smith form $G\, \mathrm{diag}(X^{U'_i(a)})\, H$ of the image of $P_i$ under $j_b$, with a rescaling identity for $1 + X D_i$.

**Theorem 4.5.3 (Weight exponents from lattices).** Let $l \neq 2$ be a prime and $k, j, t, q, h \in \mathbb{N}$ with $t + 2\lfloor h/(l-1) \rfloor < l$. Put $n = k + j + t + q$ and $\kappa = \lfloor h/(l-1) \rfloor$. Let $W$ be a Frobenius datum on a finite set $E$ with the lattice inputs for $(\sigma, l, h, u, c, U', \mathrm{wt}, \kappa)$, where $\mathrm{wt}_i(s) = b_i + s$. Let $U_i \in \mathbb{Z}^n$ and $\gamma \in \mathbb{Z}^E$, and assume for every $i$: $U_i$ and $U'_i$ are strictly decreasing, each $b_i + s$ ($s < t$) is a value of $U_i$, and $\prod_a (X + U_i(a) + \gamma_i) = \prod_a (X + U'_i(a) + \gamma_i)$ in $F[X]$. Let $\tau \in E$ with $U_\tau \geq 0$, $\sum_a U_\tau(a) = \sum_a U'_\tau(a)$ and $U_\tau(a) = b_\tau + (k + j + t - 1 - a)$ for $k + j \leq a < k + j + t$. Then
$$\begin{aligned} \sum_{a < k + j} \bigl(U_\tau(a) - U'_\tau(a)\bigr) \leq{} & q h + \Bigl(l\, m_l\bigl(b_{\sigma(\tau)}, t, \kappa; U_{\sigma(\tau)}(\cdot)\bigr) \\ & + m_l\bigl(b_\tau, t, \kappa; U_\tau(\cdot)\bigr)\Bigr)(t + 2\kappa). \end{aligned}$$

Lean: `Formalism.CohomologicalDescent.FrobeniusPeriodChange.weight_exponents_from_lattice`.

*Proof.* First the lattice inputs give the inputs over $O$: since $l \neq 2$, $u = 1 + lc$, $\zeta$ is a primitive root and the maps $j_b$ are injective on constants, the Smith forms over $L[[X]]$ at the points $\zeta^b - 1$ descend to conditions 1 to 5 of a family of weights $U'$, for $N$ and for each $N^\psi_s$. The descent uses that $O$ is complete for $I$: a series $m$ with $X^S \mid j_b(m)$ is divisible by $(X - x)^S$ for $x \in I$. The descent uses this at $x = \zeta^b - 1$. With these inputs, the bound follows from three steps: the bounds $0 \leq l\kappa_{\sigma(i)}(s) + \mathrm{wt}_i(s) - \kappa_i(s) \leq h$, the properties of the reduced data $(\Phi_i, \Gamma_i)$, and an exchange theorem that compares the sum of the first $k + j$ entries of $U_\tau$ and $U'_\tau$. The exchange uses, for the index $\tau$, that the sum of any $t$ entries of $U'_\tau$ is at least the sum of the last $t$ entries, since $U'_\tau$ is decreasing. $\square$

**Theorem 4.5.4 (Orientation by the reflection).** Let $l \neq 2$ be a prime and $t + 2\lfloor h/(l-1) \rfloor < l$. Let $D$ be a label system of length $k + j + t + q$ on $E$ that is reflexive for $(\sigma, h, t)$, linked over $F$ for $(t, \gamma)$ and carries $(\varepsilon, J, b^J)$. Let $W$ be a Frobenius datum with the lattice inputs for $(\sigma, l, h, u, c, J, \mathrm{wt}, \kappa)$, where $\mathrm{wt}_i(s) = b^J_i + s$. If $D$ has block shape at $\tau$, then $D$ satisfies the depth bound at $\tau$.

Lean: `Formalism.CohomologicalDescent.WorkedExample.orientation_lattice_holds`.

*Proof.* Since $c$ is an involution that commutes with $\sigma$, the map $\varepsilon$ is an involution that commutes with $\sigma$, and $J_i = U'_{\varepsilon(i)}$, $b^J_i = b_{\varepsilon(i)}$. For $i \notin \Phi$ we have $c(i) \in \Phi$, and the reflection identities move the linked conditions from $c(i)$ to $i$; the product identity then holds for all $i$ with the constant $0$. Apply the previous theorem to the labels $\tilde U_i = U_{\varepsilon(i)}$, $J$, $b^J$, $\gamma = 0$, and the index $\varepsilon(\tau)$. Because $\varepsilon(\varepsilon(\tau)) = \tau$ and $\sigma(\varepsilon(\tau)) = \varepsilon(\sigma(\tau))$, we get $\tilde U_{\varepsilon(\tau)} = U_\tau$, $J_{\varepsilon(\tau)} = U'_\tau$, $b^J_{\varepsilon(\tau)} = b_\tau$, $\tilde U_{\sigma(\varepsilon(\tau))} = U_{\sigma(\tau)}$ and $b^J_{\sigma(\varepsilon(\tau))} = b_{\sigma(\tau)}$. The block shape at $\tau$ gives the hypotheses at $\varepsilon(\tau)$, and the conclusion is the depth bound at $\tau$. $\square$

We now return to the notation of Section 4 ($P$, $W$, $N_r$, $k_c$, $h_0$, $U_\tau$, $b_\tau$, $\tau'_l$).

**Definition 4.5.5 (Lattice link).** Let $l$ be a prime, $\tau \in \iota$ and $w \in \mathbb{N}^{N_r}$. Put $n = k_c + j_\tau + t + q_\tau$. A *lattice link* for $(P, W, l, \tau, w)$ consists of a finite set $E$ with a permutation $\sigma$, a domain $O'$ over $\mathbb{Z}_l$ complete for an ideal $I$, a field $F$ of characteristic $l$, a field $L'$, a Frobenius datum on $E$ of rank $n$ over $(O', F)$, $u \in \mathbb{Z}_l^\times$, $c \in \mathbb{Z}_l$, a label system $D$ on $E$ of length $n$, $\gamma$, $\varepsilon$, $J$, $b^J$, $\kappa$, $\zeta$, maps $e$ and $j_b$, and a map $\mathrm{inc} : \iota \to E$, such that:

1. $D$ is reflexive for $(\sigma, h_0, t)$, linked over $F$ for $(t, \gamma)$ and carries $(\varepsilon, J, b^J)$;
2. the lattice inputs hold for $(\sigma, l, h_0, u, c, J, \mathrm{wt}, \kappa)$ with $\mathrm{wt}_i(s) = b^J_i + s$;
3. $U_{\mathrm{inc}(\tau')} = U_{\tau'}$ and $b_{\mathrm{inc}(\tau')} = b_{\tau'}$ for every $\tau' \in \iota$;
4. $\sigma(\mathrm{inc}(\tau)) = c(\mathrm{inc}(\tau'_l))$ if the reflection flag of $\tau$ at $l$ is set, and $\sigma(\mathrm{inc}(\tau)) = \mathrm{inc}(\tau'_l)$ otherwise;
5. $U'_{\mathrm{inc}(\tau)}(a) = w(a) + N_r - 1 - a$ for $a < n$, and $\sum_a U_{\mathrm{inc}(\tau)}(a) = \sum_a U'_{\mathrm{inc}(\tau)}(a)$.

**Theorem 4.5.6 (Depth from a lattice link).** Let $P$ satisfy the hypotheses and be large, and let $W$ be admissible for $P$. Let $l > l_J$ be a prime, $\tau \in \iota$ and $w \in \mathbb{N}^{N_r}$. If there is a lattice link for $(P, W, l, \tau, w)$, then
$$d_{\varpi_{k_c + j_\tau}}(\lambda_\tau|_{N_r}, w) \leq i_\tau(l).$$

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.depth_of_linkage_holds`.

*Proof.* For $l > l_J$ the size conditions on $P$ give $N_r + 1 < l$ and $t + 2\kappa_l < l$. As $N_r > 0$, $l > 2$, and $\lfloor h_0/(l-1) \rfloor = \kappa_l$. By admissibility $k_c + j_\tau + t + q_\tau = N_r$. The labels have block shape at $\mathrm{inc}(\tau)$: $U_\tau \geq 0$, the sums are equal by item 5, and $\lambda_\tau$ is constant on the block. The orientation theorem with $h = h_0$ gives the depth bound at $\mathrm{inc}(\tau)$. By item 3, $m_{\mathrm{inc}(\tau)} = m_\tau(l)$. For $\sigma(\mathrm{inc}(\tau))$ we use item 4. Without the flag, $m_{\sigma(\mathrm{inc}(\tau))} = m_{\tau'_l}(l) = m^F_\tau(l)$. With the flag, the reflection identities give $m_{c(i)} = m_i$, and the count does not change when every $u$ is replaced by $h_0 - u$ and $b$ by $h_0 - (b + t - 1)$; so again $m_{\sigma(\mathrm{inc}(\tau))} = m^F_\tau(l)$. Since $U_\tau(a) - U'_{\mathrm{inc}(\tau)}(a) = \lambda_\tau(a) - w(a)$, the left side of the depth bound is $d_{\varpi_{k_c + j_\tau}}(\lambda_\tau|_{N_r}, w)$. Hence
$$d_{\varpi_{k_c + j_\tau}}(\lambda_\tau|_{N_r}, w) \leq q_\tau h_0 + \bigl(l\, m^F_\tau(l) + m_\tau(l)\bigr)(t + 2\kappa_l).$$
The right side is an integer at most $q_\tau h + (l\, m^F_\tau(l) + m_\tau(l))(t + 2\kappa_l)$, since $h \geq 1$, so it is at most the floor $i_\tau(l)$. $\square$

**Theorem 4.5.7 (First input from lattice links).** Let $P$ satisfy the hypotheses and be large, let $W$ be admissible for $P$, let $X$ be a Hida setting for $(\iota, N_r, \lambda)$ and let $l > l_J$ be a prime. Let $\varpi \in O$, let $(L_\mu)$ be a family of $A$-modules and $\mathrm{hw}(\mu, \tau) \in \mathbb{N}^{N_r}$. Assume that for every $\mu$ such that $L_\mu$ is a subquotient of $V/\varpi V$ and the localized forms $S^{-1}\mathcal{F}(L_\mu)$ are nonzero, there is a lattice link for $(P, W, l, \tau, \mathrm{hw}(\mu, \tau))$ for every $\tau \in T_2$. Then for all such $\mu$ and all $\tau \in T_2$,
$$d_{\varpi_{k_c + j_\tau}}\bigl(\lambda_\tau|_{N_r}, \mathrm{hw}(\mu, \tau)\bigr) \leq i_\tau(l).$$

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.first_input_of_link`.

*Proof.* This is the theorem on the depth from a lattice link applied to each $\mu$ and each $\tau \in T_2$ with $w = \mathrm{hw}(\mu, \tau)$. $\square$

**Theorem 4.5.8 (Weight inputs from lattice links).** Let $P$ satisfy the hypotheses and be large, let $W$ be admissible for $P$, let $X$ be a Hida setting for $(\iota, N_r, \lambda)$ and let $l > l_J$ be a prime. Assume the weight inputs at $l$ of Section 4, with the depth bound replaced by the hypothesis of the previous theorem. Then $X$ has the weight inputs at $l$ with the budget $i(l)$.

Lean: `Formalism.CohomologicalDescent.ShortWeightBounds.weight_inputs_of_linkage_holds`.

*Proof.* This is the theorem on the first input from lattice links applied to the data $\varpi$, $(L_\mu)$ and $\mathrm{hw}$ of the hypothesis. $\square$

**Remark 4.5.9 (Formalization).** The orientation theorem and the weight exponents from lattices ask for a prime $l$ and also for $l \neq 2$, so the depth from a lattice link derives $l \neq 2$ from $N_r + 1 < l$. We read the proofs of `weight_exponents_from_inputs` and `weight_inputs_of_norm` and the statements they use, but not the proofs of the exchange theorem `weightExchangeFull_holds`, of `weight_lattice_of_norm` or of `linked_all_holds`. The matrices $\Phi_i$ and $\Gamma_i$ (`chgPhi`, `chgGam`), the series identities of the frame, the unit condition `IsUn` and the maps `inc`, `q` and `act` of the third lattice input were not unfolded. The module names do not describe the content: the orientation theorem is in [WorkedExample.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/WorkedExample.lean#L215), and the weight exponents from lattices are in HeckeLFunctionIdealEulerProduct.lean, line 1315.
