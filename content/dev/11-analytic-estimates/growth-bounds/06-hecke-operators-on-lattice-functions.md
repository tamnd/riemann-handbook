---
title: Hecke operators on lattice functions
decls:
  - Formalism.MainNotions.G.LatticeSystems.theta_kernel_expansion
  - Formalism.MainNotions.G.stability_of_trivial_stabilisers
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke operators on lattice functions

This section proves a counting statement for Hecke operators that act on functions on tuples of lattices. The statement says that a product ideal of Hecke monomials has small colength in the module of equivariant functions. It is proved for every datum with trivial stabilisers and finitely many classes, and in this form it is used by [the admissible family without kernels](/entry/admissible-family-no-kernel/) in Volume 15. The local objects are those of Section 3: the lattices of the unramified quadratic setting, edges, and the lattice families $N_{\mathrm{src}}$ and $N_{\mathrm{tgt}}$.

### Lattice functions

Let $p$ be a prime and let $\mathcal{O}$ be a [discrete valuation ring](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices) with fraction field $K$.

**Definition 5.6.1 (Places).** A *system of places* over $\mathcal{O}$ consists of an element $w \in \mathcal{O}$, integers $m, r \geq 0$, and finitely many places $v$. Each place $v$ carries an integer $n'_v$, a discrete valuation ring $W_v$ with fraction field $Q_v$, maps $\iota_v : Q_v \to K$, $\sigma_v : Q_v \to Q_v$ and $W_v \to \mathcal{O}$, a dominant weight $\lambda_{0,v}$, and an unramified quadratic setting (Section 3) for these maps and $w$. A *lattice tuple* is a family $L = (L_v)_v$ with $L_v$ a lattice in $Q_v^{m+1}$.

Let $X$ be the polynomial ring over $K$ in the entries of matrices $X_{v,s}$ of size $m+1$, for all places $v$ and $s < n'_v$. For each $v$ and each lattice $L_v$, Section 3 gives the lattice $H(L_v)$ of polynomials in the variables of $v$. Its tensor product over $v$ is a lattice $H(L) \subseteq X$.

**Definition 5.6.2 (Level).** A *level* for a system of places is a group $\Gamma$ with homomorphisms $\Gamma \to \mathrm{GL}_{m+1}(Q_v)$ for each $v$ and a character $\chi : \Gamma \to \mathcal{O}^\times$. The group acts on lattice tuples by $\gamma L = (\gamma L_v)_v$, and on $X$ by the natural action $\xi \mapsto \gamma\cdot\xi$: substitution by $\gamma^{-1}$ in each block of variables, times a power of the determinants fixed by $\lambda_{0,v}$. The level has *trivial stabilisers* if $\gamma L = L$ for a lattice tuple $L$ gives $\gamma = 1$, and *finitely many classes* if there are finitely many lattice tuples such that every lattice tuple is $\gamma L_0$ for one of them.

**Definition 5.6.3 (Data at $p$).** A *datum at $p$* is a system of places over $\mathcal{O}$ together with a finite set of components $i$, each with a level $\Gamma_i$. A *lattice function* assigns to each component $i$ and each tuple $L$ an element $F_i(L) \in X$. For a family $\mathcal{H}$ of $\mathcal{O}$-modules $\mathcal{H}(L) \subseteq X$, let $\mathcal{F}(\mathcal{H})$ be the module of lattice functions with:

1. $F_i(L) \in \mathcal{H}(L)$ for every lattice tuple $L$, and $F_i(L) = 0$ if $L$ is not a lattice tuple;
2. $F_i(\gamma L) = \chi_i(\gamma)\,\gamma\cdot F_i(L)$ for all $\gamma \in \Gamma_i$.

We write $M = \mathcal{F}(H)$ and $d = \mathrm{rank}_{\mathcal{O}}M$.

**Definition 5.6.4 (Hecke operators).** For a place $v$ and a lattice function $F$, put
$$(y_vF)_i(L) = p^{A_v}\sum_{L'' \to L_v} F_i(L[v \mapsto L'']),$$
where the sum runs over the edges $L'' \to L_v$ of Section 3, $L[v \mapsto L'']$ replaces the entry at $v$ by $L''$, and $A_v$ is the exponent $A_r(\lambda_{0,v})$ of Section 3.

The operators $y_u$ and $y_v$ commute for all places $u$, $v$. A datum is *admitted* if all its levels have trivial stabilisers and finitely many classes, and the Hecke operators commute. So a datum is admitted exactly when all its levels have trivial stabilisers and finitely many classes.

### The counting statement

For $\mathcal{O}$-modules $N \subseteq X$, an integer $g \geq 0$ and $E \geq 0$, we say that *$M$ lies in $N$ up to $g$ elements and $p^E$* if there is a finite set $C \subseteq M$ with $|C| \leq g$ such that $p^EM \subseteq N + \mathcal{O}C$. For a finite set $V$ of places and numbers $\kappa_v$, let $e_k(\kappa)$ be the elementary symmetric function of degree $k$ of the $\kappa_v$, $v \in V$.

Fix a finite set $V$ of places, integers $t_v$, $S_v$, $D$, $c^*$, $S$ and $m \geq 1$, and reals $\kappa_v$. Let $N$ be the module spanned by the monomial images
$$p^{\sum_{v \in V \setminus B}S_v}\,\Big(\prod_{v \in B}y_v^m\Big)M, \qquad B \subseteq V,$$
and put $\tau = \sum_{v \in V}m(t_v + D + 1)$ and $\Sigma = m\sum_{v \in V}\kappa_v$.

**Definition 5.6.5 (Counting statement).** A datum satisfies the *counting statement* if for all choices above with $S_v \leq S$ on $V$, and with the condition $\mathrm{LP}'(t_v, D, \kappa_v, c^*)$ of Section 3 at each $v \in V$, these hold:

1. for every $\beta \geq 0$, $M$ lies in $N$ up to $\lfloor d\,m^{\beta+1}e_{\beta+1}(\kappa)\rfloor$ elements and $p^{\tau + \beta S}$;
2. $p^{\sum_vS_v}M \subseteq N$;
3. if $\Sigma \leq 1/2$, then $d\,m^{\beta+1}e_{\beta+1}(\kappa) \leq d\,\Sigma^{\beta+1}/(\beta+1)!$ for every $\beta$, and with $N^* = N \cap p^\tau M$ the length of $M/N^*$ is at most
$$\ell(\mathcal{O}/p)\,\big(d\tau + 2S\Sigma d\big);$$
4. if $\Sigma \leq 1/2$ and $M' \subseteq M$ is saturated in $M$, then $N^* \cap M' \subseteq p^\tau M'$, the map $M'/(N^* \cap M') \to M/N^*$ is injective, and every linear map that sends $N$ into a submodule $Z$ sends $N^* \cap M'$ into $Z$.

Clause 3 says that a product ideal of Hecke monomials, cut down to $p^\tau M$, has colength linear in $d\tau$. Clause 4 says that the same bound passes to saturated submodules.

### Lemma J

For a subset $B$ of places and a choice of slot at each place, the *lattice system* is the module $\mathcal{F}$ of the family $L \mapsto \bigotimes_v\Pi_v(L_v)$, where $\Pi_v(L_v)$ is $H(L_v)$ in the base slot, $N_{\mathrm{src}}(t_v, L_v)$ in the ball slot, and the predual of $N_{\mathrm{tgt}}(t_v, L_v)$ in the dual slot. Let $\Lambda(B)$ be the system with the dual slot on $B$ and the base slot off $B$, and let $\Lambda(B, v)$ be the same with the ball slot at $v$. So $\Lambda(\emptyset) = M$.

**Definition 5.6.6 (Lemma J).** A datum satisfies *Lemma J* if, when its levels have trivial stabilisers and finitely many classes, the following holds for every nonempty $V$, all $t$, $D$, $c^*$, $\kappa$ with $\mathrm{LP}'(t_v, D, \kappa_v, c^*)$ at each $v \in V$, and every nonempty $B \subseteq V$: there is a finite set $C \subseteq \Lambda(B)$ with $|C| \leq d\prod_{v \in B}\kappa_v$ and
$$p^{D+1}\Lambda(B) \subseteq \sum_{v \in B}\mathcal{O}\,y_v\Lambda(B, v) + \mathcal{O}C.$$

So a Hecke operator at $v$ maps the ball slot onto the dual slot up to $p^{D+1}$ and a small set of exceptions.

**Lemma 5.6.7.** Lemma J and the counting statement hold for every admitted datum.

Lean: `Formalism.MainNotions.G.LatticeSystems.theta_kernel_expansion`.

*Proof.* First, Lemma J holds for every datum. Assume trivial stabilisers and finitely many classes. For a component $i$, a lattice tuple $L_0$ and $\xi \in X$, the delta function of $(i, L_0, \xi)$ is the lattice function that is $\chi_i(\gamma)\,\gamma\cdot\xi$ at $(i, \gamma L_0)$ and $0$ elsewhere; it is well defined since the stabilisers are trivial. The delta functions are linear in $\xi$, lie in $\mathcal{F}(\mathcal{H})$ when $\xi \in \mathcal{H}(L_0)$ for an equivariant family $\mathcal{H}$, and every $F \in \mathcal{F}(\mathcal{H})$ is the sum of the delta functions of its values at a finite set of representatives of the classes. The lattice systems are equivariant families. The number of representatives times $\prod_v\dim V_{\lambda_{0,v}}$ is at most $\mathrm{rank}_{\mathcal{O}}M$. So it is enough to prove the inclusion of Lemma J for delta functions at one tuple $L$, with a local set $C$ of at most $\prod_{v \in B}\kappa_v\prod_v\dim V_{\lambda_{0,v}}$ elements of $X$. This local statement follows from three facts. The first is a basis of $H(L_v)$ of size $\dim V_{\lambda_{0,v}}$ at each place. The second is a Smith form at each $v \in B$: by $\mathrm{LP}'$, the dual slot of $L_v$ has a basis in which all elements outside a set of at most $\kappa_v\dim V_{\lambda_{0,v}}$ indices, after multiplication by $p^D$, are combinations of $p^{A_v}F_k$ with $F_k$ in the ball slot at edges into $L_v$, and with $p^{A_v}F_k$ in $w^{c^*}$ times the dual slot at the other ends of these edges. The third is a step for one place: if $p^{A_v}\xi$ lies in $p^{D+1}$ times the system at the other ends of the edges, then the delta function of $p^{A_v}\xi$ lies in $\sum_v\mathcal{O}y_v\Lambda(B, v) + p^{D+1}\Lambda(B)$. Here $4(D + 1) \leq c^*$, from $\mathrm{LP}'$, controls the error terms.

Second, Lemma J gives a walk of lattice systems from the base slot through the ball and dual slots: at each $v \in V$, base is contained in ball, dual is contained in base, $w^{t_v}$ maps ball into base and base into dual, and $y_v$ maps ball into dual. The inclusions at one place follow from local facts on chains of lattices, proved with bases at the edges. With $M$ finite and free over $\mathcal{O}$, the walk gives clause 1 by induction on $\beta$, and clause 2 directly. Clause 3 follows from clause 1 and a length estimate for modules that lie in $N$ up to few elements; the inequality for $e_{\beta+1}$ is the bound $e_k(\kappa) \leq (\sum_v\kappa_v)^k/k!$ for $\kappa_v \geq 0$, and $\kappa_v \geq 0$ follows from $\mathrm{LP}'$. Clause 4 is formal. $\square$

**Theorem 5.6.8 (Stability).** Let $\mathcal{D}$ be a datum as in Section 3 such that, for every word $u$ and every place $w$ with an index, the datum at $p$ attached to $(u, w)$ has trivial stabilisers and finitely many classes. Then each of these data satisfies the counting statement.

Lean: `Formalism.MainNotions.G.stability_of_trivial_stabilisers`.

*Proof.* The Hecke operators always commute, so each datum at $p$ attached to $(u, w)$ is admitted. Apply the [Lemma 5.6.7](/entry/theta-kernel-expansion/). $\square$

The theorem is also an input of a service statement for lattices, together with the condition that the operators preserve the lattices.

**Remark 5.6.9 (Formalization).** The counting statement is `SelectionLemmas.Conclusion1` and admissibility is `SelectionLemmas.admitted` (SelectionLemmas.lean:39, 41); both ignore the datum `_D`, and so do `adm1`, `adm2` and `adm3` (lines 32 to 36). The third condition `adm3`, commutation of the `yv`, is always true by `exponent_condition_holds` (LatticeSystems.lean:593), so the hypothesis of the Lemma is only `TrivStab` and `FinClasses`. The name `theta_kernel_expansion` does not describe the content; there are two more theorems with this name (WittFrameLocaliserOrders.lean:5802, MultisetValuation/CommonEigenvectorThird.lean:32). The name `stability_of_trivial_stabilisers` also does not fit: the conclusion is `CornerGLContinuity.MLatticeCond` (CornerGLContinuity.lean:173), the counting statement at all data `D.gat u w hg`. In `counting_statement_of_block_form` (LatticeSystems.lean:2382) the hypothesis `hfin` is not used in the shown proof. The proof of Lemma J is `restJAll` (LatticeSystems.lean:4407) through `ja_restJ`, `jDelta`, `jEquiv`, `jRank`, `jLocal`, `jStep1`, `jSmith` and `jBase`; their proofs were not unfolded, and the description above follows their statements. The local chain facts `restLocD`, the walk `restWalk_of_local_J`, the clauses `walk_clause`, `esymm_clause`, `sat_clause`, `inj_clause`, the length lemma `lengthFromAllBut`, `mna_finite`, `mna_free` and the natural action `natAct` were not unfolded. In the counting statement the multiplier is $p$, not the element $w$, and the empty set $V$ is allowed.
