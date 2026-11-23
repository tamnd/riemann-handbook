---
id: weyl-cell-relation
title: The big cell relation for the Fourier transform and the Siegel parabolic
kind: theorem
decl: GlobalTheory.KSp.weyl_cell_relation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsWeilRepresentationBigCellRelationFourier
covers: 856
status: drafted
drafted_by: writer@claude
---
This lemma proves the relation that the operators of the Siegel parabolic $P$ and the scaled Fourier transform $\kappa\mathcal F$ must satisfy on the big cell $PwP$, and it fixes $\kappa$. It is the condition (b) of the generic big cell lemma in [the construction of the Weil representation](/entry/exists-is-kw/). Its second name is [the statement entry](/entry/exists-weil-representation-big-cell-relation-fourier/).

## Statement

Use the notation of [the construction](/entry/exists-is-kw/): $w = J$, the operators $\rho(p)$ for $p \in P$, the Fourier transform $\mathcal F$, and $s(z) = \chi(z)\lvert N_{E/F}z\rvert_F^{m/2}$. For a hermitian $b \in M_n(E)$ write $n(b) = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$, and for $a \in \mathrm{GL}_n(E)$ write $m(a)$ for the Levi element.

**Lemma.** There is $\kappa \neq 0$ such that for each $p \in P$ with $wpw \in PwP$ there are $p_1, p_2 \in P$ with $wpw = p_1 w p_2$ and $\kappa\mathcal F\rho(p)\kappa\mathcal F\varphi = \rho(p_1)\kappa\mathcal F\rho(p_2)\varphi$ for each $\varphi \in S$.

## Proof

1. **The Gauss constant.** [The Gauss integral of the hermitian form](/entry/has-gauss-integral-hermitian-quadratic-character/) gives $\gamma_0$ such that the regularized integral of $x \mapsto \psi(\tfrac12\mathrm{pr}(x, xb))$ is $\gamma_0\, s(\det b)^{-1}$ for each invertible hermitian $b$. The lemma `gauss_const_ne_zero`, in the same file, shows $\gamma_0 \neq 0$. Put $\kappa = s(\det(-1_n))/\gamma_0$.
2. **The decomposition.** `splitUnitarySiegelParabolic_block_relations` writes $p = m(a)\,n(b)$ with $b$ hermitian. The lower left block of $wpw$ is $ab$, and `inCell_iff_det_lower_left_block_ne_zero` turns $wpw \in PwP$ into $\det b \neq 0$.
3. **The elements.** Put $q = w\,m(a)\,w^{-1} \in P$ and $p_0 = w\,n(b)\,w\,n(-b^{-1})^{-1}w^{-1}$, whose matrix is $\begin{pmatrix} -b^{-1} & 1 \\ 0 & -b \end{pmatrix}$, so $p_0 \in P$. Then $wpw = (q p_0)\, w\, n(-b^{-1})$; take $p_1 = q p_0$ and $p_2 = n(-b^{-1})$.
4. **The operator identity.** `fourier_hermitianMultiplier_braid_relation`, with the Gauss value for $b$, gives
$$s(\det(-b^{-1}))\,\mathcal F\rho(n(b))\mathcal F = \gamma_0\, s(\det b)^{-1}\,\rho(p_0)\,\mathcal F\rho(n(-b^{-1})).$$
Since $s$ is multiplicative (`unitaryCharacterAbsScalar_basic_properties`), $\kappa\gamma_0 s(\det b)^{-1} = s(\det(-b^{-1}))$. This is the relation for $n(b)$. The factor $m(a)$ passes through $\mathcal F$ by `fourier_intertwines_siegelLeviOperator` ($\mathcal F\rho(m(a)) = \rho(q)\mathcal F$), and `parFun_sieg_mul'` joins the products in $P$.

## In the Lean code

The lemma is at [ExistsWeilRepresentationBigCellRelationFourier.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilRepresentationBigCellRelationFourier.lean#L130). The matrix computations `splitUnitaryElementMatrix_bigCell_product`, `conj_levi_mem`, `herm_neg_inv` and `lower_left` are in the same file, from line 41.

- `gauss_const_ne_zero` ([line 70](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilRepresentationBigCellRelationFourier.lean#L70)) argues by contradiction. If $\gamma_0 = 0$, the braid relation for $b = 1$ and the indicator $\varphi$ of a compact open subgroup give $\mathcal F\rho(n(1))\mathcal F\varphi = 0$. Since $\mathcal F$ is injective on $S$ ($\mathcal F^2$ is a positive multiple of a reflection) and $\rho(n(1))$ is multiplication by a function with no zeros, $\varphi = 0$. But $\varphi(0) = 1$.
- The analysis is in the braid relation and in the Gauss integral. We have not opened the proof of `fourier_hermitianMultiplier_braid_relation`.
- The value of $\kappa$ is explicit: $\kappa = s((-1)^n)/\gamma_0$.
