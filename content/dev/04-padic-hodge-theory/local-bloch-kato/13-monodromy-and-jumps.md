---
title: Monodromy and filtration jumps of a Breuil-Kisin module
decls:
  - GlobalTheory.JumpsOfM.main
  - GlobalTheory.T.filtration_jumps_breuilKisin_subset_galoisJumps
  - GlobalTheory.NgalFil.ENStable_and_jumps
  - GlobalTheory.T.breuilKisin_lattice_stable_and_hodgeTate_jumps
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Monodromy and filtration jumps of a Breuil-Kisin module

A $\varphi$-module over the Breuil-Kisin ring has a filtration by powers of $E$, and its jumps play the role of Hodge-Tate weights. This section proves two facts for a $\varphi$-module that is compared with a lattice $T$ through crystalline periods. First, the operator $E N$ maps the lattice into the module of series that converge on a closed disc. Second, every jump of the filtration of the $\varphi$-module is a Hodge-Tate jump of $T$. The input is Fontaine's theory of $B_{\mathrm{cris}}$. Both facts are used in the next section, to show that a Breuil-Kisin pack has the jumps that its type asks for.

We keep the notation of [the previous section](/entry/int-conn-taylor-main/): a prime $\ell$, integers $a, e \ge 1$ with tame descent data, a system of roots $\varpi$, the tame field $K_\varpi$, a finite extension $L$ of $\mathbb{Q}_\ell$ with ring of integers $\mathcal{O}$, $E = X^e + \ell$, and a $\varphi$-module $P$ of rank $\iota$ with matrices $Y_\tau$ and lattice $M$. Let $\nabla_P$ be its canonical connection and $N = X \nabla_P$.

**Definition 7.13.1 (Filtration and jumps of a $\varphi$-module).** Let $M[1/\ell]$ be the set of vectors with entries in $\mathfrak{S}_{\mathcal{O}}[1/\ell]$, and let $\varphi^* M[1/\ell]$ be the set of vectors $v$ such that each $v_\tau$ is an $\mathfrak{S}_{\mathcal{O}}[1/\ell]$-linear combination of the columns of $Y_\tau$. For $i \in \mathbb{Z}$ put
$$\mathrm{Fil}^i P = \big(\varphi^* M[1/\ell] \cap E^i M[1/\ell]\big) + E\, \varphi^* M[1/\ell].$$
An integer $i$ is a *jump* of $P$ if $\mathrm{Fil}^{i+1} P \ne \mathrm{Fil}^i P$.

This is the filtration of a Breuil-Kisin module by the order of $E$, seen on the image of Frobenius and taken modulo $E$. If $P$ has a basis in which $Y_\tau$ is diagonal with entries $E^{h_k}$ and $0 \le h_k$, then $\varphi^* M[1/\ell] \cap E^i M[1/\ell]$ is spanned by the $E^{\max(h_k, i)} e_k$, and the jumps of $P$ are among the $h_k$.

**Definition 7.13.2 (Monodromy and the disc).** Let $R \subseteq L[[X]]$ be the ring of series $\sum c_n X^n$ with $|c_n|\, \ell^{-n/e} \to 0$, that is, the series that converge on the closed disc $|X| \le |\ell|^{1/e}$. Let $M_R$ be the set of vectors with entries in $R$. The *monodromy operator* of $P$ is $E N = E X \nabla_P$.

The disc $|X| \le |\ell|^{1/e}$ contains the root $\varpi_0$ of $E$. So the condition $E N(M) \subseteq M_R$ says that $N$ has at most a simple pole at $E = 0$ on $M$, measured on this disc.

Now let $T$ be an $\mathcal{O}$-lattice in an $L$-representation $V$ of $G_{\mathbb{Q}_\ell}$, and let $j$ be an identification of $P$ with $T$, as in [the previous section](/entry/int-conn-taylor-main/). Fix standard period data for $\mathbb{Q}_\ell$, with de Rham ring $B_{\mathrm{dR}}$ and filtration $\mathrm{Fil}^i$, and let $B_{\mathcal{O}}$ be the crystalline period ring with coefficients in $\mathcal{O}$ (we do not unfold it). The integral period ring $A_{\mathcal{O}}$ maps both into $W_{\mathcal{O}}$ and, by a map $b$, into $B_{\mathcal{O}}$.

**Definition 7.13.3 (Crystalline comparison).** A *crystalline comparison* for $(P, j)$ is a $B_{\mathcal{O}}$-linear isomorphism $j_B : B_{\mathcal{O}}^\iota \to B_{\mathcal{O}} \otimes_{\mathcal{O}} T$ with two properties.

1. It agrees with $j$ on integral periods: if $c \in A_{\mathcal{O}}^\iota$ and $z \in A_{\mathcal{O}} \otimes T$ have the same image under $j$ in $W_{\mathcal{O}} \otimes T$, then $j_B(b(c)) = (b \otimes 1)(z)$.
2. It is horizontal: for every constant vector $d$ such that the horizontal vector $\xi(d)$ lies in the divided power lattice of $P$ with $\ell$ inverted, the element $j_B(\xi(d))$ is fixed by $G_{K_\varpi}$, acting on both factors.

Here $\xi(d)$ is the image of $d$ under the matrix $\xi_\tau$ that conjugates $d/dX$ to $\nabla_P$, so $\nabla_P\, \xi(d) = 0$.

The Hodge-Tate jumps of $V$ are the jumps of the de Rham filtration: for an embedding $\tau : \mathbb{Q}_\ell \to L$, an integer $i$ is a *Hodge-Tate jump* of $V$ at $\tau$ if $\mathrm{Fil}^{i+1} D_{\mathrm{dR}}(V) \ne \mathrm{Fil}^i D_{\mathrm{dR}}(V)$ at $\tau$. Since the base is $\mathbb{Q}_\ell$, there is one embedding $\tau$.

The input from Fontaine's theory is the following list of properties of $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$.

**Theorem 7.13.4 (Fontaine).** Let $\ell$ be a prime, and let a core of period rings be given: $B_{\mathrm{cris}}$ with its Frobenius $\varphi$, $B_{\mathrm{dR}}$ with its filtration, a map $\iota : B_{\mathrm{cris}} \to B_{\mathrm{dR}}$, and the maps from $\mathbb{Q}_\ell$, $\mathbb{Q}_\ell^{\mathrm{ur}}$ and $\overline{\mathbb{Q}}_\ell$. Then:

1. if $x_1, \dots, x_m \in \overline{\mathbb{Q}}_\ell$ are linearly independent over $\mathbb{Q}_\ell^{\mathrm{ur}}$, and $b_1, \dots, b_m \in B_{\mathrm{cris}}$ satisfy $\sum_i x_i\, \iota(b_i) = 0$, then all $b_i = 0$;
2. $\varphi$ is injective on $B_{\mathrm{cris}}$, and $\iota$ is injective;
3. if $\varphi(b) = b$ and $\iota(b) \in \mathrm{Fil}^0 B_{\mathrm{dR}}$, then $b \in \mathbb{Q}_\ell$;
4. for every $w \in B_{\mathrm{dR}}$ there is $b \in B_{\mathrm{cris}}$ with $\varphi(b) = b$ and $\iota(b) - w \in \mathrm{Fil}^0 B_{\mathrm{dR}}$;
5. for every $y \in B_{\mathrm{cris}}$ there is $x \in B_{\mathrm{cris}}$ with $\iota(x) \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ and $\varphi(x) - x = y$;
6. if $K$ is a finite extension of $\mathbb{Q}_\ell$ and $b \ne 0$ in $B_{\mathrm{cris}}$ is such that each $g \in G_K$ acts on $b$ by a scalar in $\mathbb{Q}_\ell$, then $b$ is a unit.

Parts 3 and 4 are the fundamental exact sequence $0 \to \mathbb{Q}_\ell \to B_{\mathrm{cris}}^{\varphi = 1} \to B_{\mathrm{dR}}/\mathrm{Fil}^0 \to 0$; part 1 is the injectivity of $\overline{\mathbb{Q}}_\ell \otimes_{\mathbb{Q}_\ell^{\mathrm{ur}}} B_{\mathrm{cris}} \to B_{\mathrm{dR}}$; part 6 is the regularity of $B_{\mathrm{cris}}$. See J.-M. Fontaine, "Le corps des périodes p-adiques", *Astérisque* 223 (1994), Exposé II. We take the theorem as an input.

**Theorem 7.13.5 (Filtration jumps are Hodge-Tate jumps).** Assume the theorem of Fontaine. Let $\ell \ne 2$, let $P$ be a $\varphi$-module of rank $\iota$ over $\mathcal{O}$, $T$ an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$ in $V$, $j$ an identification of $P$ with $T$, and $j_B$ a crystalline comparison for $(P, j)$ for standard period data. Assume $E N(M) \subseteq M_R$. Let $U \subseteq \mathbb{Z}$ be a set that contains every Hodge-Tate jump of $V$. Then every jump of $P$ lies in $U$.

Lean: `GlobalTheory.JumpsOfM.main` (also `GlobalTheory.T.filtration_jumps_breuilKisin_subset_galoisJumps`, a second name).

*Proof.* Let $i$ be a jump of $P$. We use two lemmas.

The first lemma uses the theorem of Fontaine, the crystalline comparison and the hypothesis on $E N$. It gives a vector $x \in V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{dR}}$ that is fixed by $G_{K_\varpi}$, with $x \in \mathrm{Fil}^i(V \otimes B_{\mathrm{dR}})$ and $x \notin \mathrm{Fil}^{i+1}(V \otimes B_{\mathrm{dR}})$. The idea: a vector of $\mathrm{Fil}^i P$ that is not in $\mathrm{Fil}^{i+1} P$ is moved by $j_B$ into $V \otimes B_{\mathrm{dR}}$, and horizontality makes it invariant.

The second lemma says: let $F$ be a finite Galois extension of $\mathbb{Q}_\ell$, and let $x \in V \otimes B_{\mathrm{dR}}$ be fixed by $G_F$, with $x \in \mathrm{Fil}^i$ and $x \notin \mathrm{Fil}^{i+1}$. Then $i$ is a Hodge-Tate jump of $V$ at every embedding. The reason is that $(V \otimes B_{\mathrm{dR}})^{G_F}$ is $D_{\mathrm{dR}}$ of $V$ over $F$, which is $F \otimes_{\mathbb{Q}_\ell} D_{\mathrm{dR}}(V)$ with the filtration extended, so a vector there whose filtration level is exactly $i$ shows that $\mathrm{Fil}^i \ne \mathrm{Fil}^{i+1}$.

The field $K_\varpi$ is Galois over $\mathbb{Q}_\ell$. Indeed, the tame descent data give $e + 1 = \ell^a$, so $e$ divides $\ell^a - 1$, and the unramified field of degree $a$ contains the $e$-th roots of unity. So $K_\varpi$ contains all roots of $X^e + \ell$, and it is the splitting field over $\mathbb{Q}_\ell$ of $X^e + \ell$ times a polynomial whose splitting field is the unramified field of degree $a$. Apply the second lemma with $F = K_\varpi$ to the vector $x$ of the first lemma. Then $i$ is a Hodge-Tate jump of $V$ at the embedding $\tau$, so $i \in U$. $\square$

**Theorem 7.13.6 (Monodromy and jumps).** Assume the theorem of Fontaine. Let $\ell \ne 2$, and let $P$, $T$, $j$ and $j_B$ be as in the previous theorem, without the hypothesis on $E N$. Then:

1. $E N(M) \subseteq M_R$;
2. for every set $U \subseteq \mathbb{Z}$ that contains every Hodge-Tate jump of $V$, every jump of $P$ lies in $U$.

Lean: `GlobalTheory.NgalFil.ENStable_and_jumps` (also `GlobalTheory.T.breuilKisin_lattice_stable_and_hodgeTate_jumps`, a second name).

*Proof.* Part 1 is a lemma on the monodromy operator: under the theorem of Fontaine, $\ell \ne 2$ and the crystalline comparison, $E N$ maps $M$ into $M_R$. Part 2 is [the theorem on filtration jumps](/entry/jumps-of-m-main/), applied with part 1 as its hypothesis. $\square$

**Remark 7.13.7 (Formalization).** The theorem on filtration jumps assumes $E N(M) \subseteq M_R$, but part 1 of the second theorem proves this from the other hypotheses, so the hypothesis is redundant. The second theorem only puts the two together. The name "lattice stable" refers to part 1, which does not say that $M$ is stable: $E N$ maps $M$ into the larger module $M_R$. The first lemma of the proof is `exists_fixed_vector_filtration_jump_breuilKisin`, the second is `isHodgeTateJump_of_galois_fixed_filtration_vector`, and part 1 is `monodromyOperator_maps_into_completion`; we read their statements, not their proofs, so the reasons given for them are the classical ones. The second lemma concludes the jump at every embedding, and the proof uses it at the embedding of $\mathbb{Q}_\ell$ into $L$ ([FiltrationJumpsBreuilKisinSubsetGaloisJumps.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FiltrationJumpsBreuilKisinSubsetGaloisJumps.lean#L17)). We did not unfold the period rings $A_{\mathcal{O}}$, $B_{\mathcal{O}}$, the core of period rings, or the standard period data.
