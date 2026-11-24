---
title: Depths and lattices of a leaf
decls:
  - GlobalTheory.BigOn.leafDepth_all_record
  - GlobalTheory.BigOn.leaves_sup_span_data
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Depths and lattices of a leaf

This section proves two groups of leaf properties for a leaf object that is a record of the runs of a datum. The first group is four bounds on the local depths at the twisted places. The second group says that the lattices of the leaf are full and stable, that the theta lattices sit inside them up to a scalar, and that the trace data lie in an eigenspace. Both are used by [the geometric statement from the page statement](/entry/geo-st-of-page-st-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). Both proofs read the needed facts off the record and pass them to general results on leaves.

A *leaf object* $O$ over a set $S$ of places and a finite group $P$, with a coefficient field $K$, consists of, for each index $j$:

- a representation $\rho_j$ of $P$ on a $K$-space $V_j$, with an $\mathcal{O}_K$-submodule $M_j$;
- for each place $v$ of a pair in $S$, three $\mathcal{O}_K$-submodules $\Theta_{v,j}$, $\Theta^K_{v,j}$, $\Theta^0_{v,j}$ of $V_j$, a scalar $\sigma_{v,j} \in K$ and a depth $e_0(v, j)$;
- a subgroup $U \subseteq P$ with a character $\psi$;

and further data that we do not need here. A submodule is *full* if it is a lattice in the whole space. The leaf object is a *record* of the runs of a datum if it is built from the runs and their ties in the way of the surjectivity chapter. We use two fields of a record: the *depth* field, which gives a star structure and the tie of the runs, and the *tied* field, which gives the laws of the core and the form ties at each place.

Let $w$ be a twisted place with residue characteristic $p_w$ and conjugate $\bar w$, and let $F_0(w, j)$ be the content of the numerical datum. Let $g_1, g_2, q_1, d$ be the four special primes of the host and let $s$ be the finite set of small primes. The four *depth bounds* are:

1. for $p_w$ not special and $p_w \leq Y$, both $e_0(w, j)$ and $e_0(\bar w, j)$ are at most $F_0(w, j) + a(j, p_w) + 1$, for a family $a \geq 0$ with a bound on $\sum_l a(j, l) \log l$; for $p_w > Y$ both depths are $0$;
2. for $p_w \in \{q_1, d\}$ both depths are at most $s_B(j) + T + 1$, with bounds on $F_0(w, j)$;
3. for $p_w \in s$ both depths are at most $s_C(j) + T + 1$, and $F_0(w, j) = 0$;
4. for $p_w \in \{g_1, g_2\}$, $e_0(w, j) \leq 2T - n(w, j)$, the same holds for $\bar w$, and $n(w, j) + n(\bar w, j) = -2 F_0(w, j)$.

Here $Y$, $T$, $s_B$, $s_C$ and $n$ are the size and level data of the leaf.

**Theorem 7.5.1 (Depths of a record).** There is a constant $C_0$ with this property. Let $O$ be a leaf object that is a record of the runs of a datum, with the page conditions and the size conditions of the leaf, with $x \geq 3$, $x^{e_z/5} \geq 3$, $k b' \leq b$ for the size data and $C_W \geq 10$ for the parameter choice. Let the content of the numerical datum equal the content of the datum, and let $C_0 \leq C$ for the constant $C$ of $O$. Then the four depth bounds hold.

Lean: `GlobalTheory.BigOn.leafDepth_all_record`.

*Proof.* [The depth bounds for a run](/entry/leaf-depth-all-run/) give the same four bounds for a leaf object with a run tie and the laws of a run, given three statements on charts of formal groups at every prime $p$: a colength bound at split places, a Hodge-Tate inclusion, and a bound for unramified companions. These three statements are proved apart from this chapter, and they fix $C_0$. The depth field of the record gives the star structure and the run tie. The tied field gives the laws of the core, and these give the laws of the run. All other hypotheses pass unchanged. $\square$

The four *lattice properties* of $O$ are:

- *support*: each $M_j$ is full and stable under $\rho_j(P)$;
- *span*: at each place $v$ of a pair, $\Theta_{v,j}$ and $\Theta^K_{v,j}$ are full;
- *scalar*: at each such $v$, $\Theta_{v,j} \subseteq M_j$, $\Theta_{v,j}$ is stable under $\rho_j(P)$, $\sigma_{v,j} \neq 0$ and $\Theta_{v,j} \subseteq \sigma_{v,j} \Theta^K_{v,j}$;
- *data*: at each such $v$, $\Theta^0_{v,j}$ is finitely generated and lies in the $\psi$-eigenspace $V_j^{U, \psi}$, and
$$|U| \cdot \mathrm{cut}\big(V_j^{U,\psi}, \Theta^K_{v,j}\big) \subseteq \Theta^0_{v,j},$$
where $\mathrm{cut}(W, \Lambda) = W \cap \Lambda$.

**Theorem 7.5.2 (Lattices of a record).** For each constant $C_K$ there is $x_1$ such that the following holds. Let $O$ be a leaf object that is a record of the runs of a datum, let each run satisfy the hypothesis on its height gaps, and let the group record of the real datum hold. Then $O$ has the support, span, scalar and data properties.

Lean: `GlobalTheory.BigOn.leaves_sup_span_data`.

*Proof.* Take $x_1 = 0$. The weight families of the record are those of the core, by the field of the record that fixes them.

For the first three properties we use a general result on leaves. It says that the support, span and scalar properties hold if chart independence holds and if, at each place $v$ and index $i$, there are a full run, its laws, a form tie with its action, a level map, the rationality of the character $\xi$, a cover, a positive own prime and three lattice facts. Chart independence holds unconditionally. The form tie and its action come from the tied field. The laws, the rationality of $\xi$ and the cover are fields of the runs. The own prime at $v$ is one of the two special primes $\mathrm{pde}$, $\mathrm{pde}'$, so it is positive. The three lattice facts are the lattice at $i$, the span at $i$ and the second height condition. They come from the hypothesis on height gaps: its lattice part, with the short span of the run, gives the lattice at $i$, and its other parts give the span and the second height condition.

For the data property we use a second general result: the span property and a tie at each place give the data property. The tie at $(v, i)$ needs the determinant of the run to be $1$ on the base level group $P_0$. The group record shows that $g \in P_0$ if and only if each component of $g$ lies in the upper unitriangular group, and the pins of the run then give determinant $1$ on $P_0$. The other parts of the tie are the full run, the laws, the rationality of $\xi$ and two facts on the weight of the last position. $\square$

**Remark 7.5.3 (Formalization).** The leaf properties are defined in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L241). The record is `IsRec` in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L55). The depth theorem is a pass through to `RunDepth.leafDepth_all_run`; of the nine fields of `IsRec` it uses only `depth` and `tied`. The three chart statements are `colength_bound_split_place_chart`, `hodgeTate_inclusion_chart` and `unramified_companion_chart_characters`. The lattice theorem uses the fields `tied`, `ok` and `kap` of the record, and the general results are `leaves_sup_span_lemmaS_of_formTieK` and `TraceLattice.leafData_of_onTie_of_leafSpan`; we read their statements. It proves the result with $x_1 = 0$, so the threshold and the constant $C_K$ play no role. Several hypotheses of the lattice theorem are not used: the core ties, the own pin, the page numbers and the size hypotheses named `tup_mu_*` are bound to `_`. The lattice facts come from `lat_span_of_hypC` at line 25 of [LeavesSupSpanData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LeavesSupSpanData.lean#L25), which drops several parts of the gap hypothesis with `-`. The predicate on the tie at a place is the constant `True`, so the tie carries no extra condition there.
