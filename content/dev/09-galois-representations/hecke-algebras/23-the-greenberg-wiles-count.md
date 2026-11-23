---
title: The Greenberg and Wiles count
decls:
  - GlobalTheory.T.greenbergWiles_dualSelmer_lower_bound_mod_prime_pow
  - GlobalTheory.Ord2.GwIneq.gw_ineq
  - GlobalTheory.T.exists_dualSelmer_classes_unbounded_order
  - GlobalTheory.Ord2.GwCount.dual_classes_unbounded
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Greenberg and Wiles count

The ordinary Selmer conditions for $W$ and for $W^*$ are exact annihilators of each other under local duality. The formula of Greenberg and Wiles compares the orders of the two Selmer groups modulo $\ell^n$. This section draws two consequences for $W$ in normal form. First, the ordinary Selmer group of $W$ modulo $\ell^n$ is at most a constant times that of $W^*$, with the constant independent of $n$. Second, if the ordinary Selmer group of $W$ does not vanish, then $W^*$ has ordinary Selmer classes modulo $\ell^n$ of unbounded order. Section 24 turns the second statement into a nonzero ordinary Selmer class of $W^*$.

We keep the notation of Sections 20 to 22. In particular $K_S$ is the kernel of $G_{\mathbb{Q}} \to G_S$, $\mathcal{O}$ is the ring of a coefficient datum, and $a \equiv_n b$ means $|a - b| \leq |\ell^n|$, coordinatewise for vectors.

### Selmer cocycles modulo $\ell^n$

Let $V$ be $W$ or $W^*$, with entries in $\mathcal{O}$.

**Definition 6.23.1 (Selmer cocycle modulo $\ell^n$).** A map $z : G_{\mathbb{Q}} \to \mathcal{O}^2$ is an *ordinary Selmer cocycle for $V$ modulo $\ell^n$* if:

1. $z$ is continuous and $z(st) \equiv_n z(s) + V(s)z(t)$ for all $s, t$;
2. $z(a) \equiv_n 0$ for $a \in K_S$;
3. for each $q \in S$ with $q \neq \ell$ there are a place $B$ over $q$ and $x \in \mathcal{O}^2$ with $z(s) \equiv_n V(s)x - x$ for $s \in I_B$;
4. there is $x \in \mathcal{O}$ with $z(s)_2 \equiv_n V(s)_{22}\,x - x$ for $s \in D_A$.

Two such cocycles $z, z'$ are *cohomologous modulo $\ell^n$* if there is $x \in \mathcal{O}^2$ with $z(s) - z'(s) \equiv_n V(s)x - x$ for all $s$.

So a Selmer cocycle modulo $\ell^n$ is a cocycle of $G_S$ with values in $M_n = (\mathcal{O}/\ell^n)^2$ that is unramified at the primes of $S$ other than $\ell$ and ordinary at $\ell$. Classes modulo cohomology form the Selmer group $H^1_{\mathcal{L}}(G_S, M_n)$ for these local conditions, at least up to the passage between cocycles with values in $\mathcal{O}^2$ and in $M_n$.

### The inequality

**Theorem 6.23.2 (Greenberg and Wiles inequality).** Assume the cohomological inputs of Section 21. Let $W$ be in normal form for $(e, S, A)$, and let $\mathcal{O}$ contain the entries of $W$. There is $C$ with the following property. Let $n \geq 1$ and let $y_1, \ldots, y_N$ be ordinary Selmer cocycles for $W$ modulo $\ell^n$, pairwise not cohomologous modulo $\ell^n$. Then there are $N'$ with $N \leq CN'$ and ordinary Selmer cocycles $z_1, \ldots, z_{N'}$ for $W^*$ modulo $\ell^n$, pairwise not cohomologous modulo $\ell^n$.

Lean: `GlobalTheory.Ord2.GwIneq.gw_ineq` (also `GlobalTheory.T.greenbergWiles_dualSelmer_lower_bound_mod_prime_pow`, a second name).

*Proof.* Since $W$ is unramified outside $S$, it is trivial on $K_S$. So $W$ defines an action $\rho_n$ of $G_S$ on $M_n$. Choose a character of $G_S$ modulo $\ell^n$ that lifts the cyclotomic character; it identifies the Tate dual $\mathrm{Hom}(M_n, \mu_{\ell^n})$ with $M_n$ under $W^*$. For each real place choose a complex conjugation $c_\infty$.

Let $\mathcal{L}$ be the local conditions: at $v \in S$ with $v \neq \ell$ the unramified classes, and at $\ell$ the ordinary classes. Let $\mathcal{L}^*$ be the dual conditions for $M_n^*$. The formula of Greenberg and Wiles, among the cohomological inputs, reads
$$
\frac{\#H^1_{\mathcal{L}}(G_S, M_n)}{\#H^1_{\mathcal{L}^*}(G_S, M_n^*)} = \frac{\#H^0(G_S, M_n)}{\#H^0(G_S, M_n^*)}\cdot\frac{1}{\#H^0(\mathbb{R}, M_n)}\cdot\prod_{v \in S}\frac{\#\mathcal{L}_v}{\#H^0(\mathbb{Q}_v, M_n)}.
$$
We bound the factors.

1. For $v \neq \ell$ the unramified classes satisfy $\#\mathcal{L}_v = \#H^0(\mathbb{Q}_v, M_n)$, so these factors are $1$.
2. Since $\det W(c_\infty) = -1$ and $\ell$ is odd, $c_\infty$ has eigenvalues $1$ and $-1$, and $\#H^0(\mathbb{R}, M_n) = \#(\mathcal{O}/\ell^n)$.
3. At $\ell$, there is $C_A$, independent of $n$, with $\#\mathcal{L}_\ell \leq C_A\,\#(\mathcal{O}/\ell^n)$.
4. There is $C_0$, independent of $n$, with $\#H^0(G_S, M_n) \leq C_0$.

The factor $\#H^0(G_S, M_n^*)$ is at least $1$, and so is $\#H^0(\mathbb{Q}_\ell, M_n)$. Together,
$$
\#H^1_{\mathcal{L}}(G_S, M_n) \leq C_0C_A\,\#H^1_{\mathcal{L}^*}(G_S, M_n^*).
$$
Put $C = C_0C_A$.

Two more facts connect these groups with cocycles. The classes of $y_1, \ldots, y_N$ in $H^1_{\mathcal{L}}(G_S, M_n)$ are distinct, since cohomologous classes there give cocycles cohomologous modulo $\ell^n$; so $N \leq \#H^1_{\mathcal{L}}(G_S, M_n)$. Each class of $H^1_{\mathcal{L}^*}(G_S, M_n^*)$ is represented by an ordinary Selmer cocycle for $W^*$ modulo $\ell^n$, and distinct classes give cocycles that are not cohomologous modulo $\ell^n$. Let $N' = \#H^1_{\mathcal{L}^*}(G_S, M_n^*)$ and let $z_1, \ldots, z_{N'}$ be such representatives. Then $N \leq CN'$. $\square$

Fact 3 is where the ordinary condition enters: the local Euler characteristic formula gives $\#H^1(\mathbb{Q}_\ell, M_n) = \#(\mathcal{O}/\ell^n)^2$ up to bounded factors, and the ordinary condition is about half of it. Fact 4 holds because $W$ is irreducible, so the invariants of $M_n$ stay bounded as $n$ grows. The formula is due to Wiles; see A. Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Ann. of Math. 141 (1995), 443 to 551, and H. Darmon, F. Diamond and R. Taylor, *Fermat's Last Theorem*, Theorem 2.19.

### Dual classes of unbounded order

**Theorem 6.23.3 (Dual classes of unbounded order).** Assume the cohomological inputs. Let $W$ be in normal form for $(e, S, A)$, and assume that the ordinary Selmer group of $W$ does not vanish. Then there is a coefficient datum with ring $\mathcal{O}$ that contains the entries of $W$ such that, for each $m \geq 0$, there are $n$ and an ordinary Selmer cocycle $z$ for $W^*$ modulo $\ell^n$ such that $\ell^mz$ is not cohomologous to $0$ modulo $\ell^n$.

Lean: `GlobalTheory.Ord2.GwCount.dual_classes_unbounded` (also `GlobalTheory.T.exists_dualSelmer_classes_unbounded_order`, a second name).

We use three facts.

**Lemma 6.23.4 (Bounded torsion of a class).** Let $Y$ be a cocycle for $W$ with values in $\mathcal{O}^2$ that is not a coboundary. There is $k_0$ such that, for all $n$ and $a \in \mathcal{O}$, if $aY$ is cohomologous to $0$ modulo $\ell^n$, then $a\,\ell^{k_0} \equiv_n 0$.

**Lemma 6.23.5 (Vanishing on $K_S$).** A cocycle for $W$ that is a coboundary on $I_B$ for a place $B$ over each prime $q \notin S$ vanishes on $K_S$.

**Lemma 6.23.6 (Bounded torsion classes).** For each $m$ there is $B_m$ with the following property. For all $n$, a family of ordinary Selmer cocycles for $W^*$ modulo $\ell^n$ that are pairwise not cohomologous modulo $\ell^n$, each with $\ell^mz_i$ cohomologous to $0$ modulo $\ell^n$, has at most $B_m$ members.

The first lemma holds because the cohomology of the compact group $G_S$ with values in $\mathcal{O}^2$ is finitely generated over $\mathcal{O}$. The third lemma comes from the finiteness of $H^1(G_S, M_m)$: classes killed by $\ell^m$ are controlled by classes modulo $\ell^m$.

*Proof of the theorem.* Let $y$ be an unramified cocycle of $W$, ordinary at $A$, that is not a coboundary. By the scaling lemma of Section 22 there are a ring $\mathcal{O}$ and $k$ such that $Y = \ell^ky$ has values in $\mathcal{O}^2$, is an integral coboundary on inertia away from $\ell$, and is ordinary at $A$ with an integral $x$. The cocycle $Y$ is not a coboundary. Let $k_0$ be as in the first lemma. By the second lemma, $Y$ vanishes on $K_S$.

Fix $m$. Let $C$ be the constant of the inequality, $B_m$ that of the third lemma, and $t = CB_m + 1$, so that $CB_m < \ell^t$. Put $n = t + k_0$, and for $0 \leq j < \ell^t$ let $y_j = jY$. Each $y_j$ is an ordinary Selmer cocycle for $W$ modulo $\ell^n$, since $Y$ is an exact cocycle with integral local trivializations. For $i \neq j$, the difference $y_i - y_j = (i - j)Y$ is not cohomologous to $0$ modulo $\ell^n$. Indeed, otherwise the first lemma gives $(i - j)\ell^{k_0} \equiv_{t + k_0} 0$, so $\ell^t \mid i - j$, which is false since $0 < |i - j| < \ell^t$.

The inequality gives $N'$ with $\ell^t \leq CN'$ and pairwise non-cohomologous ordinary Selmer cocycles $z_1, \ldots, z_{N'}$ for $W^*$ modulo $\ell^n$. If $\ell^mz_i$ were cohomologous to $0$ for every $i$, the third lemma would give $N' \leq B_m$, so $\ell^t \leq CB_m$, a contradiction. So some $z_i$ has $\ell^mz_i$ not cohomologous to $0$ modulo $\ell^n$. $\square$

**Remark 6.23.7 (Formalization).** The second names are wrappers of the form `first | exact @… | …`. The wrapper of the inequality also tries the helper `GlobalTheory.Ord2.GwIneq.exists_cc`, which chooses complex conjugations and has a different type; that alternative cannot succeed ([GreenbergWilesDualSelmerLowerBoundModPrimePowStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GreenbergWilesDualSelmerLowerBoundModPrimePowStatement.lean#L9)). In the inequality the formula of Greenberg and Wiles is a field of the cohomological inputs, and the four bounds are `GlobalTheory.Ord2.UrCard.card_unramified_h1_eq_card_h0`, `GlobalTheory.T.archimedean_invariants_card`, `GlobalTheory.T.card_ordinaryLocalConditionModPrimePow_le_const_mul` and `GlobalTheory.T.card_galoisInvariants_ordinaryRankTwo_mod_pow_bounded`. The passage between classes and cocycles is `GlobalTheory.T.ordinarySelmerModPrimePow_injects_residualSelmer` and `GlobalTheory.T.dualSelmer_classes_give_noncohomologous_cochains`. In the second theorem the three lemmas are `GlobalTheory.T.nonzero_class_bounded_torsion`, `GlobalTheory.T.cocycle_vanishes_on_ker_toGS_of_inertia_coboundary` and `GlobalTheory.T.card_primePowTorsion_selmerClassesModPrimePow_bounded` (with `GlobalTheory.T.card_dualCocyclesModPrimePow_unramifiedOutsideS_bounded_alt`). We read all of them as statements; the explanations of the bounds and the form of the displayed formula are ours.
