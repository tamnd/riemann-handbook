---
title: Bernoulli bounds for odd characters
decls:
  - UpperTheory.V.ML.iv
  - UpperTheory.V.ML.psiOf
  - UpperTheory.V.ML.vChar
  - lev_case
  - prim_case
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernoulli bounds for odd characters

This section proves the character bound of Section 2: for an odd prime $l$, a Dirichlet character $\psi$ of order prime to $l$ and $e \geq 1$ with $\psi(-1) = (-1)^{e + 1}$, the length of the Tate-Shafarevich group of the twist of $O \otimes \mathbb{Q}_l/\mathbb{Z}_l$ by $\chi_O^{-e}\psi^{-1}$ is at most the valuation of a multiple of the generalized Bernoulli number $B_{e + 1, \psi}$. For a primitive character this is the [Kolyvagin bound](/entry/ml-count/) applied to the twisting character $\chi_O^{-e}\psi^{-1}$, together with a congruence between the Stickelberger value and the Bernoulli number. A character of any level reduces to its primitive character. The bound then passes to the eigenspaces of an abelian CM field. With Poitou-Tate duality it gives the input of [Theorem 4.2.12](/entry/thm-bc-free-of/) for the minus part, which feeds the count in [Theorem 8.16.7](/entry/of-four-alt/). The background is in [Dirichlet characters](/learn/l-functions/#dirichlet-characters) and [the cyclotomic character and Tate modules](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

### The lengths of single characters

Let $l$ be an odd prime and let $O$ be a complete discrete valuation ring, finite over $\mathbb{Z}_l$, inside $\overline{\mathbb{Q}}_l$. A Dirichlet character $\psi$ modulo $N$ with values in $O$ defines a character $\psi_G : G_\mathbb{Q} \to O^\times$ through $\mathrm{Gal}(\mathbb{Q}(\zeta_N)/\mathbb{Q}) \cong (\mathbb{Z}/N)^\times$. For $e \geq 1$ put $\Psi_e = \chi_O^e \psi_G$.

**Definition 4.5.1 (The length of a character).** Let $V_l(e, \psi)$ be the length over $O$ of the Tate-Shafarevich group over $\mathbb{Q}$ attached to $O \otimes \mathbb{Q}_l/\mathbb{Z}_l$ twisted by $\Psi_e^{-1}$, with the local conditions at $l$ of the window bound.

**Definition 4.5.2 (Bernoulli value).** For a Dirichlet character $\chi$ modulo $N$ and $k \geq 1$, put $a_{N,k}(\chi) = N \cdot (k + 1)\# \cdot B_{k, \chi}$, as in Section 2, where $B_{k, \chi}$ is the generalized Bernoulli number of the primitive character attached to $\chi$.

The factor $N \cdot (k + 1)\#$ clears the denominators: by the theorem of von Staudt and Clausen and its generalization to characters, $a_{N,k}(\chi)$ is integral over $\mathbb{Z}$. When the level of $\chi$ grows from $f$ to a multiple $N$, the primitive character does not change and $a_{f,k}$ divides $a_{N,k}$ in the ring of integers, since $f \cdot (k+1)\#$ divides $N \cdot (k+1)\#$.

### Primitive characters

**Theorem 4.5.3 (Bernoulli bound, primitive case).** Assume the reciprocity law of Section 4. Let $\psi$ be a primitive Dirichlet character of conductor $f$ with values in $O$, of order prime to $l$, let $e \geq 1$ with $\psi(-1) = (-1)^{e + 1}$, and let $a \in O$ be equal to $a_{f, e+1}(\psi)$. Then
$$V_l(e, \psi) \leq v_O(a).$$

Lean: `prim_case`.

*Proof.* Put $\alpha = \Psi_e^{-1}$. Since $\psi$ is primitive of order prime to $l$, it is ramified at each prime $p \mid f$ with a value $\psi_G(g) - 1$ a unit on the inertia at $p$, it is unramified outside $f$, and $\psi_G(g) - 1$ is a unit whenever $\psi_G(g) \neq 1$: a root of unity of order prime to $l$ that is not $1$ is not congruent to $1$.

Case 1: there is $g$ with $\alpha(g) - \chi_O(g)$ a unit. Let $f_0$ be the part of $f$ prime to $l$. For each nonzero $a_0 \in O$, the congruence between Stickelberger elements and Bernoulli numbers gives $m \geq 1$, $b < f_0 l^m$ and lifts $\sigma_t$ with these properties: $\alpha$ is a twisting character for $(f_0, m)$, $a_0 \, z(\alpha, \sigma, b) \mid l^m$, and $z(\alpha, \sigma, b) \mid a$. The congruence is the classical one: modulo $l^m$, the sum $\sum_t \vartheta(t) \Psi_e(\sigma_t)$ is $\sum_t \vartheta(t) t^e \psi(t)$, which is a unit multiple of $(1 - \psi(b) b^{e+1}) B_{e+1, \psi}/(e+1)$ after the choice of $b$. Let $\delta$ lift $-1$ modulo $f_0 l^m$. The twisting condition gives $\alpha(\delta) \equiv -1 \pmod{l^m}$, so $\alpha(\delta) - 1 \equiv -2$ is a unit, as $l$ is odd. Each class of the Tate-Shafarevich group gives a cocycle in the strict Selmer group $\mathrm{Sel}(\alpha, \delta, f l, a_0)$ for a suitable $a_0$, since $\alpha$ is unramified outside $fl$ and has unit values $\alpha(g) - 1$ on the inertia at the primes of $f$ prime to $l$. So $V_l(e, \psi)$ is at most the supremum over $a_0 \neq 0$ of the lengths of these Selmer groups. The places over $fl$ are the places over $f_0 l^m$, so the Selmer group at level $fl$ equals the one at level $f_0 l^m$. The [Kolyvagin bound](/entry/ml-count/) gives length at most $v_O(z(\alpha, \sigma, b)) \leq v_O(a)$.

Case 2: $\alpha(g) - \chi_O(g)$ is a non-unit for every $g$. Then $\alpha$ is congruent to $\chi_O$ modulo the maximal ideal. At a place not over $l$, $\chi_O$ is trivial on inertia, so the inertia values of $\psi_G$ are $\equiv 1$; by the unit property above they are $1$. So $\alpha$ is unramified outside $l$. In this case the Tate-Shafarevich group is zero: a class would give an unramified extension of the field cut out by $\alpha$ on which Galois acts through the cyclotomic character modulo the maximal ideal, and the local conditions at $l$ exclude it. So $V_l(e, \psi) = 0 \leq v_O(a)$. $\square$

### Characters of any level

**Theorem 4.5.4 (Bernoulli bound, change of level).** Assume the reciprocity law. Let $f \mid N$, let $\varphi$ be a primitive character of conductor $f$, and let $\psi$ be the character modulo $N$ induced by $\varphi$. Suppose $\psi$ has order prime to $l$, $e \geq 1$ and $\psi(-1) = (-1)^{e + 1}$, and let $a \in O$ be equal to $a_{N, e+1}(\psi)$. Then $V_l(e, \psi) \leq v_O(a)$.

Lean: `lev_case`.

*Proof.* The Galois characters of $\psi$ and $\varphi$ are equal, so $V_l(e, \psi) = V_l(e, \varphi)$. The order and the parity of $\varphi$ are those of $\psi$. The Bernoulli number of $\psi$ is that of its primitive character $\varphi$, and $a_{f, e+1}(\varphi)$ divides $a_{N, e+1}(\psi)$ in $O$, since $f \cdot (e+2)\#$ divides $N \cdot (e+2)\#$. The primitive case gives $V_l(e, \varphi) \leq v_O(a_{f, e+1}(\varphi)) \leq v_O(a)$. $\square$

**Theorem 4.5.5 (Bernoulli bound for odd characters).** Assume the reciprocity law. Let $l$ be odd, let $\psi$ be a Dirichlet character modulo $N$ with values in $O$, of order prime to $l$, let $e \geq 1$ with $\psi(-1) = (-1)^{e + 1}$, and let $a \in O$ be equal to $a_{N, e+1}(\psi)$. Then
$$V_l(e, \psi) \leq v_O(a).$$

Lean: `UpperTheory.V.ML.vChar`.

*Proof.* This is the Theorem on change of level applied to the primitive character of $\psi$, whose conductor divides $N$. $\square$

### Eigenspaces over abelian CM fields

**Theorem 4.5.6 (The character bound).** Assume the reciprocity law. Then the character bound of Section 2 holds: for each abelian CM field $E$ with cyclotomic action $\rho$ modulo $N$, each odd prime $l \nmid [E : \mathbb{Q}]$, each $O$, $e \geq 1$, and $\psi : \mathrm{Gal}(E/\mathbb{Q}) \to O^\times$ with $\psi(\rho(-1)) = (-1)^{e + 1}$, and each $a = a_{N, e+1}(\psi \circ \rho)$, the length $\ell_\psi(E, e)$ is at most $v_O(a)$.

Lean: `UpperTheory.V.ML.psiOf`.

*Proof.* Put $\chi = \psi \circ \rho$, a Dirichlet character modulo $N$. Its order divides the order of $\psi$, which divides $[E : \mathbb{Q}]$, so it is prime to $l$, and $\chi(-1) = (-1)^{e + 1}$. The Theorem for odd characters gives $V_l(e, \chi) \leq v_O(a)$. The Galois character of $\chi$ is $\psi$ composed with the restriction $G_\mathbb{Q} \to \mathrm{Gal}(E/\mathbb{Q})$, since $\rho$ is the cyclotomic action. The $\psi$-eigenspace of the Tate-Shafarevich group over $E$ is the Tate-Shafarevich group over $\mathbb{Q}$ of the twist by $\psi$, by restriction and corestriction, which are inverse up to the unit $[E : \mathbb{Q}]$ on the eigenspace because $l \nmid [E : \mathbb{Q}]$. So $\ell_\psi(E, e) = V_l(e, \chi) \leq v_O(a)$. $\square$

**Corollary 4.5.7 (The character bound from duality).** Assume Poitou-Tate duality and the orthogonality of unramified classes. Then the character bound holds.

Lean: `UpperTheory.V.ML.iv`.

*Proof.* This is the Theorem on the character bound applied to the reciprocity law, which holds by the Theorem of Section 4 on the reciprocity law. $\square$

**Remark 4.5.8.** The bound is one half of the main conjecture of Iwasawa theory for the odd eigenspaces at a fixed finite level: the length of an eigenspace is at most the valuation of a Bernoulli number. Mazur and Wiles proved the equality; the inequality by Euler systems is due to Kolyvagin and Rubin.

**Remark 4.5.9 (Formalization).** The two theorems `prim_case` ([PrimCase.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/PrimCase.lean#L89)) and `lev_case` (line 165) are private and sit in the root namespace, not in `UpperTheory.V.ML`. The module `PrimCase` holds `UpperTheory.V.ML.vChar` (line 201) as its public theorem. A private lemma at line 19 has the long name `valuation_natCast_le_one_primitive_frobenius_fixed`. [Iv.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/Iv.lean#L4) is a one-line composition of `UpperTheory.V.ML.psiOf` with `UpperTheory.V.ML.recip`. The length $V_l(e, \psi)$ is `Chr.V`, defined through a representation `rho` that is not unfolded here; the local conditions at $l$ are those of `ShaU`, also not unfolded. The Stickelberger congruence is the lemma `UpperTheory.V.ML.zEval` and the vanishing in Case 2 is `UpperTheory.V.ML.exc`; their proofs are not unfolded here, and the arguments given for them are the classical ones.
