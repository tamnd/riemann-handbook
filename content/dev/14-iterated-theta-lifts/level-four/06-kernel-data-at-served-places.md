---
title: Kernel data at served places
decls:
  - GlobalTheory.Mem.Top.KerOne.levels_cls_cmp_at_served
  - GlobalTheory.T.served_place_levels_classes_comparison_maps
  - GlobalTheory.Mem.Top.KerOne.kerData_at_served
  - GlobalTheory.T.levels_kernelData_at_served_place
  - GlobalTheory.Mem.Top.Bl.gyLay_kerT_entC
  - GlobalTheory.T.exists_latticeLayer_kernelDatum_trueColumns
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernel data at served places

The kernel entry conditions of the previous section are statements at the level-free places of the coefficient field. To use them in the construction of the core, we must put them into a local form at each served place. At a served place $v$ the stage datum gives a local group datum at the residue prime $p$ of $v$, with a finite set of local places, lattice tuples and levels. A kernel datum at $v$ is a set of local objects that reads the classes of the stages through lattice tuples, compares the global lattices with the local ones, and carries a kernel power series. In this section we first build the levels, the class maps and the comparison maps at a served place. Then we build a kernel datum that agrees with a given entry datum. Last, we put these local data together into a lattice instance and a kernel certificate for each pinned column datum. The background is in Volume 1, at [places and completions](/learn/number-fields/#places-and-completions), [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups) and [discrete valuation rings and lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices).

### The setting

Let $K$ be a context over the base $B$, with the forced primes. Let $w$ be a pinned column datum over $B$ with frame $f$ and twist data $T$. Fix a later stage $Z$ and let $D$ be the stage datum of $w$ at $Z$, with $m$ stages and the column parameter $t$. We take the following data.

1. Column data at split primes for $w$ and $Z$.
2. A set $W_t$ of places of the base and a tied choice for $w$, $Z$ and $W_t$, such that the character $\mu$ of the stage is given by $W_t$.
3. A divisor datum $Y$ for $D$ whose primes are those that the column choices of $w$ allow.
4. Lift objects $O(u,a)$ that are standard and unfolded at every stage $i < m$.
5. An entry datum $E$ for $D$, $Y$ and the twisted forms, that is compatible with $O$.

**Definition 1.6.1 (Served place).** Let $u$ be a word. A place $v$ of the coefficient field is served for $u$ if its residue characteristic $p$ is a prime with $p \ge 5$, $p$ is inert in the host, the host is nonzero at $p$, $p$ is not one of the level primes of the host, and $p$ does not divide the level $T_u$ of the member at $u$.

At a served place $v$ for $u$ the stage datum gives a local group datum $G_{u,v}$ at $p$. It has a finite set of local places $q$, a local field $Q_q$ at each $q$, a ring of integers $\mathcal{O}$ and a field $K_f$. A lattice tuple is a family of lattices, one in $Q_q^{m_0+1}$ for each $q$.

**Definition 1.6.2 (Fills and levels).** A fill of $G_{u,v}$ is a choice of base weights and of lifted weights $w_j(q,s)$ for $j \ge 1$, which increase in $j$ and give dominant weights at each stage. The fill gives a local datum $P_j$ at each stage $j$, of rank $m_0 + j(t+1) + 1$. A family of levels for a fill is, for each $j$, a finite set $C_j$ of components and a level at $P_{j+1}$ for each component. A level has a lattice $M$ and a group $\Gamma$ that acts on the lattice tuples. The integral forms $\mathrm{Int}(j)$ at stage $j$ are the functions on components and tuples with values in the lattices $M$.

We also fix a fill $F_{u,v}$ for each word $u$ and each served place $v$, such that its parameter is $t$, its number of stages is $m$, and its lifted weights are $w_j(q,s) = \mathrm{wj}_j(\mathrm{pos}(q,s)) - \kappa_j$ for each lift index $j$. Here $\mathrm{pos}$ is the position of the local place in the orbit that the column data give, and $\kappa_j$ is the shift of the size data.

### Levels, classes and comparison maps

**Theorem 1.6.3 (Levels, classes and comparison maps at a served place).** Assume the setting above. Let $u$ be a word and $v$ a served place for $u$. Then there are a family of levels $L_v$ for $F_{u,v}$, class maps

$$
\mathrm{cl}_j : C_j \times \mathrm{Tup}(P_{j+1}) \to \mathrm{Cl}_{j+1}(u, \mu_v),
$$

and comparison maps $\mathrm{cmp}_j$ from the global forms space at stage $j+1$ to the local forms at stage $j+1$, such that for each $j$ with $j + 1 \le m$ the following hold.

1. For components $a, a'$ and lattice tuples $L, L'$, we have $\mathrm{cl}_j(a,L) = \mathrm{cl}_j(a',L')$ if and only if $a = a'$ and $L' = \gamma L$ for some $\gamma$ in the group of the level at $a$.
2. Each class at stage $j+1$ is $\mathrm{cl}_j(a,L)$ for some $a$ and some lattice tuple $L$.
3. The $\mathcal{O}$-span of the image of the global lattice at stage $j+1$ under $\mathrm{cmp}_j$ is $\mathrm{Int}(j+1)$.

Here $\mathrm{Cl}_{j+1}(u, \mu_v)$ is the set of classes at stage $j+1$ for the twisted character at $u$ and at the tuple $\mu_v$ of $v$.

Lean: `GlobalTheory.Mem.Top.KerOne.levels_cls_cmp_at_served` (also `GlobalTheory.T.served_place_levels_classes_comparison_maps`, a second name)

*Proof.* Step 1 (Comparison data). We get comparison data along the stages: the levels $L_v$, a family of inputs at each stage, the hypotheses on these inputs, the fact that the character at each stage is the twisted character at $u$ and $\mu_v$, a condition on each stage, and the fact that the component sets $C_j$ are empty for $j \ge m$. There are two cases. If $\mu_v$ is the reference tuple $\mu_0$, we use the comparison data of the steps up to the rank. If $\mu_v \neq \mu_0$, we use the comparison data for a tuple that is not the reference tuple.

Step 2 (Steps). From the comparison data and the rationality of the relative blocks, we get a sequence of steps. Each step has a semilinear comparison map, a proof that it is injective, and a proof that it is rational.

Step 3 (Class maps). For $j + 1 \le m$, the stage input at $j$ has a core, and the core gives a class of each pair $(a, L)$. We move this class to $\mathrm{Cl}_{j+1}(u,\mu_v)$ along the equality of characters from step 1. For $j + 1 > m$, the set $C_j$ is empty, so there is nothing to define.

Step 4 (The three properties). The move along the equality of characters is a bijection. So property (1) follows from the criterion for equal classes of the core, which uses the stage condition from step 1. Property (2) follows from the surjectivity of the core classes. Property (3) is the integrality of the steps, which follows from the descent of the comparison data. The comparison maps are the maps of the steps. Because they are injective and rational, they are linearly independent on the bases of the global forms. $\square$

### Kernel data

**Definition 1.6.4 (Kernel datum at a served place).** A kernel datum at a served place $v$ for $u$, with levels $L_v$, has the following parts.

1. A place map $\lambda$ from the algebraic numbers in $\mathbb{C}$ to $\mathbb{C}_p$, and an embedding $\iota_K : K_f \to \mathbb{C}_p$ that agrees with $\lambda$ on the coefficient field.
2. Embeddings $\iota_{j,q}$ of the host field $E$ into the local fields $Q_q$ at each stage.
3. For each stage $j$, component $a$ and lattice tuple $L$, a global module over $\mathcal{O}_E$ whose localizations at the places $q$ are the lattices $L(q)$.
4. Class maps at each stage, with the properties (1) and (2) of the theorem above.
5. A power series $\mathrm{Th}_j$ over $\mathbb{C}_p$ for each pair of a component and tuple at stage $j$ and a component and tuple at stage $j+1$.
6. Comparison maps with property (3) of the theorem above.

A kernel datum gives a kernel at $p$. The kernel agrees with $E$ at $v$ if it has the place map of $E$ at $v$ and if, in local bases with unit determinant, each kernel series $E.\mathrm{Th}$ at the classes of $(a,L)$ and $(a',L')$ is the linear transform of $\mathrm{Th}_j$ by unit scalars of norm $1$.

**Theorem 1.6.5 (Kernel data at a served place).** Assume the setting above. Let $u$ be a word and $v$ a served place for $u$. Then there are levels $L_v$ for $F_{u,v}$ and a kernel datum $\mathrm{KD}$ at $v$ with these levels, such that the following hold.

1. The place map of $\mathrm{KD}$ is the place map of $E$ at $v$.
2. The kernel of $\mathrm{KD}$ at $p$ agrees with $E$ at $v$.
3. The kernel of $\mathrm{KD}$ is compatible with the symmetric group data of the column data at $v$.
4. The kernel of $\mathrm{KD}$ satisfies the positivity condition at $v$.

Lean: `GlobalTheory.Mem.Top.KerOne.kerData_at_served` (also `GlobalTheory.T.levels_kernelData_at_served_place`, a second name)

*Proof.* Step 1 (Embedding). There is an embedding $\iota_K$ of the local coefficient field into $\mathbb{C}_p$ that agrees with the place map of $E$ at $v$ on the coefficient field.

Step 2 (Stage zero). The classes at stage zero are the local orbit pairs. That is, there is a class map at stage zero with the properties (1) and (2).

Step 3 (Later stages). The theorem above gives the levels $L_v$, the class maps at the stages $j + 1$ and the comparison maps with property (3).

Step 4 (Global modules). At each stage we use the same embeddings $\iota_{j,q}$ of $E$, which the split place idempotents of the column data give. For a lattice tuple $L$, there is a global module over $\mathcal{O}_E$ whose localizations are the lattices $L(q)$. We choose one such module for each tuple. For a family that is not a lattice tuple we take the zero module, but this value is not used.

Step 5 (Assembly). With steps 1 to 4 we get a kernel datum $\mathrm{KD}_0$ whose kernel series are $0$. By the existence of free kernel series at a served place, there is a family $\mathrm{Th}$ of power series such that the kernel datum $\mathrm{KD}$, which is $\mathrm{KD}_0$ with the series $\mathrm{Th}$, agrees with $E$ at $v$. This gives (1) and (2).

Step 6 (Symmetry and positivity). The symmetric compatibility (3) is the compatibility of the split place idempotents with the CM embeddings. The positivity (4) is the statement that the split place embedding at an orbit position is the induced embedding. $\square$

### The lattice instance and the kernel certificate

A lattice instance for $D$ has, for each word and each served place, a fill, levels and a chain of maps. A kernel certificate for the column data, $Y$, a lattice instance and a kernel family is a choice of standard and unfolded lift objects $O$ and of an entry datum $E$ compatible with $O$, such that at each word $u$ and served place $v$ the kernel of the family has the place map of $E$, agrees with $E$, is symmetric and is positive.

**Theorem 1.6.6 (A lattice instance and a kernel certificate).** Eventually in the context, at all large bases, each pinned column datum $w$ has the following property. For each later stage $Z$ and each choice of data (1), (2) and (3) of the setting, there are a lattice instance $G_y$ for $D$ and a kernel family for $G_y$ such that:

1. the lattice layer conditions hold for $G_y$: its ramified parts are defined by the comparison maps, its fills are the given ones, and $G_y$ is tied to each canonical instance;
2. there is a kernel certificate with lift objects $O$ and entry datum $E$;
3. there are place embeddings, place matrices $B$ and a proof $h$ of the kernel entry conditions for $O$, $B$ and $Y$, such that $E$ is the entry datum that $B$ and $h$ give.

Lean: `GlobalTheory.Mem.Top.Bl.gyLay_kerT_entC` (also `GlobalTheory.T.exists_latticeLayer_kernelDatum_trueColumns`, a second name)

*Proof.* Step 1 (Cloud bound). Eventually in the context, for each later stage there is a number $c$ that bounds the clouds of all words and is at most the constant $c_G(L)$ of each valid size datum $L$. We add this bound to the hypotheses.

Step 2 (Lift objects). The true column choices of $w$ give standard and unfolded lift objects $O$ for the laws of $w$, $Z$ and the primes of $Y$. We choose place embeddings.

Step 3 (Adapted bases). The jets of the pin and the theorem on adapted bases for the kernel datum of true column choices give place matrices $B$, a proof $h$ of the kernel entry conditions, and the compatibility of the entry datum $E$ of $B$ and $h$ with $O$. This theorem uses the kernel entry conditions of the previous section, after a rescaling of the place matrices.

Step 4 (Lattice layer). The intrinsic lattice layer theorem for true columns, with the cloud bound of step 1, gives a vertex map, fills $F_{u,v}$ with the correct parameter and the correct number of stages, the correct lifted weights, and the tie to the canonical instances for each choice of levels.

Step 5 (Local kernel data). The theorem above, applied at each word $u$ and served place $v$, gives levels $L_v$ and a kernel datum $\mathrm{KD}_{u,v}$ with the properties (1) to (4).

Step 6 (Assembly). Let $G_y$ be the lattice instance with the vertex map and the fills of step 4 and the levels of step 5, whose chains and ramified parts come from the comparison maps of the kernel data $\mathrm{KD}_{u,v}$. Let the kernel family be the family of kernels at $p$ of the $\mathrm{KD}_{u,v}$. The ramified parts of $G_y$ are those of the comparison maps by construction, the fills and the tie come from step 4, and the kernel certificate comes from steps 2, 3 and 5. The last equation holds by the definition of $E$. $\square$

The theorem is step 2 of the construction of the core in the last section of this part.

**Remark 1.6.7 (Formalization).** In `kerData_at_served`, the embeddings and the global modules are defined by a `match` on the stage $j$ whose two branches are the same ([LevelsKernelDataAtServedPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelsKernelDataAtServedPlace.lean#L44)). The first kernel datum has the zero series `Th := fun _ _ _ => 0` (line 88), and the free series theorem then replaces it. In `gyLay_kerT_entC`, the instance is first written with zero chains and zero ramified parts, and `withFirst` replaces both ([ExistsLatticeLayerKernelDatumTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLatticeLayerKernelDatumTrueColumns.lean#L33)). The place embeddings come from `Classical.choice`. The comparison data in the two cases of $\mu_v$, the core classes, the stage zero classes, the global modules, the free series, the adapted bases, the cloud bound and the intrinsic lattice layer are cited through statement files.
