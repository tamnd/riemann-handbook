---
title: Cuspidal representations of general linear groups
decls:
  - DiscreteGroups.sglob.LConv.cuspGen
  - DiscreteGroups.sglob.LConv.localConverseGL
  - GlobalTheory.cuspidalMirabolic_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cuspidal representations of general linear groups

This section collects three local facts on cuspidal representations of $\mathrm{GL}_n$. Over a nonarchimedean local field, every cuspidal representation has a Whittaker functional, and a cuspidal representation of $\mathrm{GL}_{m+1}$ is determined by its epsilon factors of pairs with the irreducible representations of $\mathrm{GL}_m$; this is the local converse theorem of Henniart. Over a finite field, cuspidal representations exist in every rank, and their restriction to the mirabolic subgroup is the representation induced from a generic character. These facts are the local side of [Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions), and they are used in [the step on every character](/step/every-character-of-literature/).

### Notation

Let $k$ be a nonarchimedean local field and $\psi : k \to \mathbb{C}^\times$ a nontrivial continuous additive character with values of absolute value $1$. Let $N_n$ be the group of upper triangular unipotent matrices in $\mathrm{GL}_n(k)$ and $\psi_n(u) = \psi(\sum_i u_{i,i+1})$. A representation $\pi$ of $\mathrm{GL}_n(k)$ on a complex vector space is *smooth* if each vector has an open stabilizer. It is *cuspidal* if it is smooth and its Jacquet module for the unipotent radical of every proper standard parabolic subgroup is $0$. A linear form $l$ is a *$\psi$-Whittaker functional* if $l(\pi(u) v) = \psi_n(u) l(v)$ for $u \in N_n$, and $\pi$ is *generic* if it has a nonzero one.

### Cuspidal representations are generic

**Theorem 1.6.1 (Cuspidal representations are generic).** Let $\pi$ be a cuspidal representation of $\mathrm{GL}_n(k)$ on a nonzero space $V$. Then $\pi$ has a nonzero $\psi$-Whittaker functional.

Lean: `DiscreteGroups.sglob.LConv.cuspGen`.

*Proof.* For $1 \le m \le n$ let $N^{(m)}$ be the set of $u \in N_n$ whose first $m$ columns are those of the identity, with the character $\chi_m(u) = \psi(\sum_{i+1 \ge m} u_{i,i+1})$ (columns counted from $0$), and let $K_m$ be the span of the vectors $\pi(u) v - \chi_m(u) v$ for $u \in N^{(m)}$. Then $N^{(1)} = N_n$ and $\chi_1 = \psi_n$. We show by downward induction on $m$ that $K_m \neq V$. For $m \ge n$, $N^{(m)}$ is trivial and $K_m = 0$. Suppose $K_{j+1} \neq V$ with $1 \le j < n$. The entries of column $j$ above the diagonal form an abelian group, and since $\pi$ is smooth there is a character $\xi$ of this group, given by a vector $\xi \in k^n$, such that adding the corresponding twisted kernel to $K_{j+1}$ still gives a proper subspace. If $\xi_i = 0$ for all $i < j$, then the twisted kernel lies in the kernel of the Jacquet module for the parabolic subgroup of type $(j, n-j)$, which is all of $V$ by cuspidality; this is impossible. So some $\xi_p \neq 0$ with $p < j$. Conjugating by an elementary matrix that moves $\xi$ to a vector with nonzero entry in row $j-1$, and then by a matrix that normalizes $N^{(j+1)}$, one reaches the standard character, and $K_j \neq V$. Finally, take a nonzero linear form $l$ that vanishes on $K_1$. Then $l(\pi(u) v) = \psi_n(u) l(v)$ for all $u \in N_n$. $\square$

Note that the theorem does not ask $\pi$ to be irreducible.

### The local converse theorem

Let $w_n$ be the antidiagonal permutation matrix, $\tilde{g} = w_n\, {}^t g^{-1}$, and embed $\mathrm{GL}_m$ in $\mathrm{GL}_{m+1}$ by $g \mapsto \operatorname{diag}(g, 1)$. A *Whittaker test function* on $\mathrm{GL}_m(k)$ is a locally constant function $f$ with $f(u g) = \psi_m(u) f(g)$ for $u \in N_m$ that vanishes outside $N_m C$ for a compact set $C$. An *invariant integral* is a linear form $I$ on functions that are left $N_m$-invariant, locally constant, and compactly supported modulo $N_m$, such that $I(f(\cdot\, x)) = I(f)$ for all $x$.

**Definition 1.6.2 (Epsilon factor of a pair).** Let $\pi$ be a representation of $\mathrm{GL}_{m+1}(k)$ and $\tau$ a representation of $\mathrm{GL}_m(k)$. A number $e$ is an *epsilon factor of $(\pi, \tau)$ for $\psi$* if for every central character $\omega$ of $\tau$, every $\psi$-Whittaker functional $l$ of $\pi$, every $\psi^{-1}$-Whittaker functional $l'$ of $\tau$, every invariant integral $I$ and all vectors $v, v'$,
$$I\Big(g \mapsto l\big(\pi(\widetilde{\operatorname{diag}(g,1)}) v\big)\, l'\big(\tau(\tilde{g}) v'\big)\Big) = \omega(-1)^m\, e\, I\Big(g \mapsto l\big(\pi(\operatorname{diag}(g,1)) v\big)\, l'\big(\tau(g) v'\big)\Big).$$

This is the local functional equation of Jacquet, Piatetski-Shapiro and Shalika at the center, written without the complex variable.

**Theorem 1.6.3 (Local converse theorem for $\mathrm{GL}_{m+1}$).** Let $k$ have characteristic $0$, $m \ge 1$, and let $\pi_1$, $\pi_2$ be smooth irreducible cuspidal representations of $\mathrm{GL}_{m+1}(k)$. Suppose that for every smooth irreducible representation $\tau$ of $\mathrm{GL}_m(k)$ there is one number $e$ that is an epsilon factor of both $(\pi_1, \tau)$ and $(\pi_2, \tau)$ for $\psi$. Then $\pi_1 \cong \pi_2$.

Lean: `DiscreteGroups.sglob.LConv.localConverseGL`.

The proof combines four inputs.

1. (Generic.) Cuspidal representations have nonzero Whittaker functionals, by the theorem above.
2. (Kirillov bump.) For a smooth representation $\rho$ of $\mathrm{GL}_{m+1}(k)$ and a vector $v_0$ there is $v$ with $l(v) = l(v_0)$ for every $\psi$-Whittaker functional $l$, and with $l(\rho(\operatorname{diag}(g,1)) v) = 0$ for all $g$ whenever $l(v_0) = 0$.
3. (Big cell.) Let $\pi_1, \pi_2$ be smooth irreducible with $\psi$-Whittaker functionals $l_1, l_2$. Suppose that whenever the Whittaker functions $g \mapsto l_i(\pi_i(\operatorname{diag}(g,1)) v_i)$ agree on $\mathrm{GL}_m(k)$, also $l_1(\pi_1(w_{m+1}) v_1) = l_2(\pi_2(w_{m+1}) v_2)$; and suppose there is such a pair with $l_1(v_1) \neq 0$. Then $\pi_1 \cong \pi_2$.
4. (Separation.) If $k$ has characteristic $0$, there is an invariant integral $I$ on $\mathrm{GL}_m(k)$ such that a Whittaker test function $f$ for $\psi$ with $I(f \cdot W) = 0$ for every Whittaker function $W$ of every smooth irreducible $\tau$ for $\psi^{-1}$ is $0$.

The separation input is proved from four further facts: extreme invariant forms exist; a positive invariant form that is extreme is, on each invariant subspace, either $0$ or nondegenerate modulo that subspace; the dimension of the $K$-fixed vectors of smooth irreducible representations is bounded uniformly for each open compact $K$, by a bound on commutative algebras of operators; and from this bound, through an alternating identity, unitary irreducible representations are admissible. Only the separation input uses that $k$ has characteristic $0$.

*Proof.* By input 1 choose nonzero $\psi$-Whittaker functionals $l_1, l_2$. We check the two hypotheses of input 3.

Let $v_1, v_2$ have Whittaker functions that agree on $\mathrm{GL}_m(k)$. Let $f(g) = l_1(\pi_1(\widetilde{\operatorname{diag}(g,1)}) v_1) - l_2(\pi_2(\widetilde{\operatorname{diag}(g,1)}) v_2)$. Since $\pi_1$ and $\pi_2$ are cuspidal, $f$ is a Whittaker test function for $\psi^{-1}$. Let $\sigma$ be smooth irreducible, $l$ a $\psi$-Whittaker functional of $\sigma$ and $v$ a vector. Put $\theta(g) = w_m\, {}^t g^{-1} w_m$; the representation $\sigma \circ \theta$ is smooth irreducible, has a central character $\omega$, and $l$ is a $\psi^{-1}$-Whittaker functional for it. Apply the hypothesis to $\tau = \sigma \circ \theta$ and the vector $v' = \sigma(\theta(w_m))^{-1} v$, for which $\tau(\tilde{g}) v' = \sigma(g) v$. The two functional equations, for $\pi_1$ and $\pi_2$ with the same $e$, have equal right sides because the Whittaker functions of $v_1$ and $v_2$ agree on $\mathrm{GL}_m(k)$. So $I(f \cdot (g \mapsto l(\sigma(g) v))) = 0$. By input 4, $f = 0$. At $g = 1$, $\widetilde{\operatorname{diag}(1,1)} = w_{m+1}$, which gives $l_1(\pi_1(w_{m+1}) v_1) = l_2(\pi_2(w_{m+1}) v_2)$.

For the second hypothesis, choose $a_i$ with $l_i(a_i) = 1$ and apply input 2 to $\pi_1 \times \pi_2$ and $v_0 = (a_1, a_2)$. For the Whittaker functional $l_1 \circ \mathrm{pr}_1$ we get $l_1(v_1) = 1$. For $l_1 \circ \mathrm{pr}_1 - l_2 \circ \mathrm{pr}_2$, which vanishes at $v_0$, the Whittaker functions of $v_1$ and $v_2$ agree on $\mathrm{GL}_m(k)$. Input 3 gives $\pi_1 \cong \pi_2$. $\square$

### Cuspidal representations over a finite field

Now let $k$ be a finite field with $q$ elements. A representation of $\mathrm{GL}_N(k)$ is *cuspidal* if it has no nonzero vector fixed by the unipotent radical of a proper standard parabolic subgroup. The *mirabolic subgroup* $P_{n+1}$ is the group of matrices in $\mathrm{GL}_{n+1}(k)$ whose last row is $(0, \dots, 0, 1)$, and $N_{n+1} \subseteq P_{n+1}$ is the upper triangular unipotent subgroup. For a nontrivial character $\psi_0$ of $k$, let $\psi_0(u) = \psi_0(\sum_i u_{i,i+1})$ on $N_{n+1}$, and let $\operatorname{Ind}(\psi_0)$ be the space of functions $f$ on $P_{n+1}$ with $f(u x) = \psi_0(u) f(x)$, with $P_{n+1}$ acting by right translation.

**Theorem 1.6.4 (Cuspidal representations over a finite field).** Let $k$ be a finite field and $n \ge 0$.

1. There is an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional space.
2. For each nontrivial character $\psi_0$ of $k$ and each irreducible cuspidal representation $\rho$ of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional space, the restriction of $\rho$ to $P_{n+1}$ is isomorphic to $\operatorname{Ind}(\psi_0)$.

Lean: `GlobalTheory.cuspidalMirabolic_holds` (also `CompanionTheory.Mirab.cuspidalMirabolic`, the proof it calls).

*Proof.* Part 1 is built from a monic irreducible polynomial of degree $n+1$ over $k$ and a cuspidal label attached to it. For part 2, an irreducible cuspidal $\rho$ on $V$ has $\dim V = \prod_{i=1}^{n} (q^i - 1)$ and a nonzero linear form $L$ with $L(\rho(u) x) = \psi_0(u) L(x)$ for $u \in N_{n+1}$. Let $T(x)(p) = L(\rho(p) x)$ for $p \in P_{n+1}$. Then $T(x) \in \operatorname{Ind}(\psi_0)$ and $T$ intertwines the restriction of $\rho$ with $\operatorname{Ind}(\psi_0)$. The representation $\operatorname{Ind}(\psi_0)$ is irreducible, by a Mackey argument. The image of $T$ is a nonzero subrepresentation, since $T(x)(1) = L(x)$, so $T$ is onto. The dimension of $\operatorname{Ind}(\psi_0)$ is the index of $N_{n+1}$ in $P_{n+1}$, which is $\prod_{i=1}^{n}(q^i - 1) = \dim V$. So $T$ is an isomorphism. $\square$

**Remark 1.6.5 (Formalization).** The local converse theorem is `DiscreteGroups.sglob.LConv.localConverseGL_of_leaves` applied to twelve named inputs: `cuspGen`, `kirBump`, `bigCell`, `extremeExists`, `extremeIrred`, `sepOfExtreme`, `commBound`, `unifOfComm`, `altIdentity`, `finiteOfAlt`, `unitOfUnif` and `glue`, all in the namespace `DiscreteGroups.sglob.LConv`. We opened `glue` (LConvGlue.lean, line 148) and `cuspGen`, with its step lemma, but not the proofs of the other inputs; their statements are in LConvCut.lean. In the step of `cuspGen` the column character comes from `DiscreteGroups.sglob.LConvGenF.exists_col_char`, whose proof we did not open. The epsilon factor of a pair is `GlobalTheory.LocLanglands.HasPairEps`; it has no complex variable. For the finite field, part 1 is `GlobalTheory.CompanionTheory.Hypotheses₂.cuspidalExists_holds` and the dimension formula is `CompanionTheory.Mirab.Restr.finrank_and_whit`, which rests on `GlobalTheory.CompanionTheory.TyFin.ColStep.cuspWh`; we did not open these proofs. The wrappers `UpperTheory.LiteratureTheorems.local_converse_gl_of_literature` and [`cuspidal_mirabolic_of_literature`](/entry/cuspidal-mirabolic-of-literature/) take an argument they do not use and return the theorems of this section.
