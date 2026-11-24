---
title: The Kolyvagin bound
decls:
  - UpperTheory.V.ML.count
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kolyvagin bound

This section proves the main inequality of the Euler system method for the system of Gauss sums: the length of a Selmer group of a twisting character $\alpha$ is at most the valuation of the Stickelberger value $z(\alpha, \sigma, b)$. The proof is Kolyvagin's induction. The Kolyvagin system of [Theorem 4.3.11](/entry/nu-sys-ex/) gives classes whose ramification at a new prime $q$ equals their value at Frobenius before $q$ was added, and a reciprocity law turns this into a bound for the classes of the Selmer group at $q$. Choosing the primes $q$ by Chebotarev's theorem lowers the length at each step. The result is used in the next section for the characters of conductor prime to $l$ in [Theorem 4.5.3](/entry/prim-case/). We keep the notation of the previous section: $l$ is odd, $O$ is a complete discrete valuation ring finite over $\mathbb{Z}_l$, $W = O \otimes \mathbb{Q}_l/\mathbb{Z}_l$, and $v_O$ is the normalized valuation.

### Cocycles and the Selmer group

A *cocycle* for a character $\alpha : G_\mathbb{Q} \to O^\times$ is a locally constant function $c : G_\mathbb{Q} \to W$ with $c(gh) = c(g) + \alpha(g) c(h)$. It is the cocycle of a class in [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology) $H^1(\mathbb{Q}, W(\alpha))$.

**Definition 4.4.1 (Strict Selmer group).** Let $\alpha : G_\mathbb{Q} \to O^\times$, let $\delta \in G_\mathbb{Q}$, let $F \geq 1$ and $a \in O$. The *strict Selmer group* $\mathrm{Sel}(\alpha, \delta, F, a)$ is the $O$-module of cocycles $c$ for $\alpha$ such that:

1. $c(\delta) = 0$ and $a c = 0$;
2. $c$ vanishes on the inertia group of each place not over $F$;
3. for each place $A$ over $F$ there is $m \in W$ with $a m = 0$ and $c(g) = \alpha(g) m - m$ for $g \in D_A$.

If $\alpha(\delta) - 1$ is a unit, each class has exactly one cocycle with $c(\delta) = 0$, since a coboundary $g \mapsto (\alpha(g) - 1)m$ is fixed by its value at $\delta$. So the module is the group of classes killed by $a$ that are unramified outside $F$ and locally trivial at $F$. For $n \geq 1$ let $\mathrm{Sel}_n$ be the submodule of the cocycles that also vanish on $D_A$ for every place $A$ over $n$.

### The reciprocity law

The induction needs one statement of global duality. It pairs a class $c$ for $\alpha$ with a class $n$ for the dual character $\alpha^* = \chi_O \alpha^{-1}$, as the sum of the local invariants of their cup products vanishes.

**Definition 4.4.2 (The reciprocity law).** The *reciprocity law* is the following statement. Let $l$ be odd, $O$ as above, $\alpha : G_\mathbb{Q} \to O^\times$, and $a \neq 0$ in $O$ with $\{g : a \mid \alpha(g) - 1\}$ open. Let $w_0 \in W$ have annihilator $(a)$. Let $N \neq 0$ with $l \mid N$, and let $q \neq l$ be a prime. Let $c$ be a cocycle for $\alpha$ and $n$ a cocycle for $\alpha^*$, both killed by $a$. Suppose:

1. at each place not over $Nq$, the inertia group acts with $a \mid \alpha - 1$, and $c$ and $n$ vanish on it;
2. at each place over $N$ and not over $q$, $c$ is a local coboundary of an element killed by $a$;
3. at a place $A_0$ over $q$, $a$ divides $\alpha(g) - 1$ and $\alpha^*(g) - 1$ for $g \in D_{A_0}$, and $c$ vanishes on $I_{A_0}$.

Then for $g \in D_{A_0}$, $\tau \in I_{A_0}$ and $y \in O$ with $n(\tau) = y w_0$, we have $y \, c(g) = 0$.

Under these conditions both characters are trivial modulo $a$ on $D_{A_0}$, the local pairing at $q$ is the product of the unramified value $c(\mathrm{Frob})$ and the tame value $n(\tau)$, and the other local terms vanish. So the law is the statement that this one local term is zero.

**Theorem 4.4.3 (The reciprocity law).** Assume Poitou-Tate duality and the orthogonality of unramified classes under local Tate duality. Then the reciprocity law holds.

Lean: `UpperTheory.V.ML.recip`.

*Proof.* This is global reciprocity for the cup product of $c$ and $n$: by Poitou-Tate duality the sum over all places of the local invariants of $c \cup n$ is zero, and at each place except $A_0$ the conditions make both classes unramified or one of them locally trivial, so the local term vanishes by the orthogonality of unramified classes. $\square$

### The bound

**Theorem 4.4.4 (Kolyvagin bound).** Assume the reciprocity law. Let $\alpha$ be a twisting character for $(N_0, m)$ with $F = N_0 l^m$, let $b < F$, and let $\delta \in G_\mathbb{Q}$ with $\alpha(\delta) - 1$ a unit. Let $\sigma_t$ lift $t$ for each $t \in (\mathbb{Z}/F)^\times$, and let $a_0 \in O$ with $a_0 \, z(\alpha, \sigma, b) \mid l^m$. Then
$$\mathrm{length}_O \, \mathrm{Sel}(\alpha, \delta, F, a_0) \leq v_O\big(z(\alpha, \sigma, b)\big).$$

Lean: `UpperTheory.V.ML.count`.

*Proof.* Put $z = z(\alpha, \sigma, b)$ and $J = v_O(l^m)$. Since $a_0 z \mid l^m$, $z \neq 0$, and $l^m = z k$ with $a_0 \mid k$. Choose $w \in W$ with annihilator $(l^m)$. By Dirichlet's theorem choose a prime $r \equiv 1 \pmod F$ and a place $A_0$ over $r$. The [Theorem 4.3.11](/entry/nu-sys-ex/) on Kolyvagin systems gives a system $(\nu_L)$ for $(l, l^m, F, r, \alpha^*, A_0, z w)$. For each admissible list $L$, let $a_L$ be the annihilator of the values of $\nu_L$ on $G_F$; it divides $l^m$ and is nonzero.

The start relation gives $\tau_0 \in I_{A_0}$ with $\nu_{()}(\tau_0) = u z w$, a unit multiple of $z w$, whose annihilator is $(k)$.

The key step is the following. Let $n \geq 1$, let $q \equiv 1 \pmod F$ be a prime with a place $A$ over $q$ and a Frobenius $\phi$ at $A$, and let $\nu$ be a Kolyvagin class for $(l^m, F, Fnq, \alpha^*)$ with values of annihilator $(a')$. Let $\tau \in I_A$ with $\nu(\tau)$ of annihilator $(a)$, and suppose $a_0 \mid a$. Then $a' = a e$ for some $e \in O$, $e$ kills $c(\phi)$ for every $c \in \mathrm{Sel}_n$, and
$$\mathrm{length} \, \mathrm{Sel}_n \leq \mathrm{length} \, \mathrm{Sel}_{nq} + v_O(e).$$
Indeed, the reciprocity law applied to $c \in \mathrm{Sel}_n$ and the class $\nu$ (which is a cocycle for $\alpha^*$ on $G_\mathbb{Q}$ after inflation) shows that the annihilator of $\nu(\tau)$ kills $c(\phi)$. Since $q \equiv 1 \pmod F$, $A$ is not over $F$, and $c$ is unramified at $A$; so $c|_{D_A}$ is determined by $c(\phi)$. The map $c \mapsto c(\phi)$ from $\mathrm{Sel}_n$ has kernel $\mathrm{Sel}_{nq}$, and its image lies in a cyclic module of length at most $v_O(e)$.

The induction runs over the admissible lists $L$ with $a_0 \mid a_L$, with the quantity
$$\mathrm{length}\,\mathrm{Sel}_{r \prod L} + v_O(a_L) .$$
The base case is $L = ()$: the key step at $q = r$ with $\tau_0$ bounds the length of $\mathrm{Sel}_1 = \mathrm{Sel}(\alpha, \delta, F, a_0)$ by the length of $\mathrm{Sel}_r$ plus $v_O(e_0)$, where $a_{()} = k e_0$, so that $v_O(e_0) = v_O(a_{()}) - v_O(k) \leq J - v_O(k) = v_O(z)$ up to the term $v_O(a_{()})$ carried by the induction. For the inductive step, suppose $\mathrm{Sel}_{r \prod L} \neq 0$ and take a nonzero $c$ in it. By the Chebotarev density theorem applied to the field cut out by $c$, by $\nu_L$ and by the roots of unity of order $F$ and $l^m$, there is an admissible prime $q$ not in $L$ such that $c(\phi_q) \neq 0$ and $\nu_L(\phi_q)$ has the same annihilator as all values of $\nu_L$. The step relation gives $\tau \in I_A$ with $\nu_{q :: L}(\tau)$ a unit times $\nu_L(\phi_q)$, so the key step applies to $\nu_{q :: L}$ with $a = a_L$. Then $v_O(a_{q :: L}) > v_O(a_L)$, since $c(\phi_q) \neq 0$ forces $e$ to be a non-unit, and the length drops by at most $v_O(e)$. So the quantity does not decrease while $v_O(a_L)$ strictly increases. Since $v_O(a_L) \leq J$ for every $L$, the induction stops after at most $J$ steps, at a list with $\mathrm{Sel}_{r \prod L} = 0$. Comparing the quantity at the start and at the end gives the bound $v_O(z)$. $\square$

**Remark 4.4.5.** The bound has the form of the inequality of Kolyvagin and Rubin for the minus part of class groups of cyclotomic fields: the order of an eigenspace of the class group is at most the order of the corresponding Bernoulli number. Here the module is a Selmer group of a single twisting character, and the Bernoulli number enters through the Stickelberger value $z$.

**Remark 4.4.6 (Formalization).** The theorem is in [FrobFix.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/FrobFix.lean#L143); the module is named after a private lemma `frob_fix` (line 63). The key step is the private lemma `key` (line 68) and the module $\mathrm{Sel}_n$ is the private definition `Sn` (line 38). A private lemma `not_over` at line 60 has the same name as an unrelated private lemma in `WeakShimuraTheory/CompactIntegralFields/NotOver.lean` (line 14). The reciprocity law is the definition `Rec` in [IsAdmissiblePrimeListNil.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/IsAdmissiblePrimeListNil.lean#L141); its proof `UpperTheory.V.ML.recip` from Poitou-Tate duality and unramified orthogonality is in `OverIff.lean` (line 297) and is not unfolded here. The Chebotarev choice of $q$ and the lemma `shtNu` used in the inductive step are not unfolded here either.
